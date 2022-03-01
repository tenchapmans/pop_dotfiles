import time
import platform

p = platform.system()

if p == 'Linux':
    from ewmh import EWMH
    import psutil
    import Xlib

def get_active_window():
    if p == 'Linux':
        return linux_get_active_window()
    raise 'Platform %s not supported' % p

def get_list_of_all_windows():
    if p == 'Linux':
        return linux_get_list_of_all_windows()
    raise 'Platform %s not supported' % p

def linux_get_list_of_all_windows():
    ret = set()
    ewmh = EWMH()
    for window in ewmh.getClientList():
        try:
            win_pid = ewmh.getWmPid(window)
        except TypeError:
            win_pid = False
        if win_pid:
            app = psutil.Process(win_pid).name()
        else:
            app = 'Unknown'
        wm_name = window.get_wm_name()
        if not wm_name:
            wm_name = 'class:{}'.format(window.get_wm_class()[0])
        ret.add((app, wm_name))
    return ret

def linux_get_active_window():
    ret = set()
    ewmh = EWMH()
    active_window = ewmh.getActiveWindow()
    if not active_window:
        return '', ''
    try:
        win_pid = ewmh.getWmPid(active_window)
    except TypeError:
        win_pid = False
    except Xlib.error.XResourceError:
        return '', ''
    wm_name = active_window.get_wm_name()
    if not wm_name:
        wm_name = 'class:{}'.format(active_window.get_wm_class()[0])
    if isinstance(wm_name, bytes):
        wm_name = wm_name.decode('utf-8')
    if win_pid:
        active_app = psutil.Process(win_pid).name()
    else:
        return '', wm_name
    return (active_app, wm_name)

