#! /usr/bin/env python
                
def test_cmdline ():
    print ('--- testing b_cmdline')
    from bptbx import b_cmdline
    if 'windows' in b_cmdline.get_platform():
        command = 'cmd.exe'
        command_exe = command +  ' /C dir'
    else:
        command = 'ls'
        command_exe = command + ' ~/'
    
    assert b_cmdline.check_for_command(command)
    code, _, _ = b_cmdline.execute_command(command_exe, True, True)    
    assert code == 0
    assert b_cmdline.get_command_process(command)
        
def test_daemon():
    print ('--- testing b_daemon')
    from bptbx import b_daemon
    from threading import Thread 
    from time import sleep 
    
    class TestDaemon(b_daemon.Daemon):
        runs = 0
        def _run_daemon_process(self):
            print ('daemon running. iteration #{}'.format(self.runs+1))
            self.runs += 1
    
    def start_daemon(daemon):
        daemon.start()
        
    daemon = TestDaemon(1)
    thread = Thread(target=start_daemon, args = (daemon,))
    thread.start()
    sleep(2)
    assert daemon.runs > 0
    daemon.stop()
    
def test_enum ():
    print ('--- testing b_enum')
    from bptbx import b_enum
    my_enum = b_enum.enum ('START', 'STOP')
    assert my_enum.START == 0
    assert my_enum.STOP == 1
    assert b_enum.Filetype.FILE == 0
    assert b_enum.Filetype.DIR == 1    

def test_iotools():
    print ('--- testing b_iotools')
    from bptbx import b_iotools
    
    assert (b_iotools.basename('/somewhere/on/the/disc/filetype.css', '.css')
     == 'filetype')
    assert (b_iotools.basename('/somewhere/on/the/disc/filetype.css') 
    == 'filetype.css')    
    assert b_iotools.countlines('LICENSE') == 202
    assert b_iotools.file_exists('LICENSE') 
    assert len(b_iotools.filedatetime()) == 2
    assert len(b_iotools.finddirs('.')) > 0
    assert len(b_iotools.findfiles('.')) > 0
    assert len(b_iotools.findfiles('.', '120410hd1212re')) == 0
    assert len(b_iotools.get_immediate_subdirectories('.')) > 0
    assert len(b_iotools.get_immediate_subfiles('.')) > 0
    assert b_iotools.getuidfromfilepath('LICENSE') == 'LICENSE'
    b_iotools.import_module_with_check('numpy')
    b_iotools.import_modules_with_check( [ 'numpy', 'math' ])
    assert b_iotools.insertintofilename('test.txt', 'foo') == 'testfoo.txt'
    assert b_iotools.md5sum('LICENSE') == '175792518e4ac015ab6696d16c4f607e'
    assert (b_iotools.read_config_section_to_keyval_list(
                'test-data/config.txt', 'AlbumInfo') == [('key', 'Value')])
    assert (b_iotools.read_config_section_to_keyval_list(
                'test-data/config.txt', 'TextInfo') == [('foo', 'Bar')])
    assert len(b_iotools.read_file_to_list('LICENSE')) == 202
    b_iotools.zip_dir_recursively('test-data', 'test-data/zip.zip')
    assert b_iotools.file_exists('test-data/zip.zip')
    b_iotools.remove_silent('test-data/zip.zip')
    assert not b_iotools.file_exists('test-data/zip.zip') 
    
def test_legacy():
    print ('--- testing b_legacy')
    from bptbx import b_legacy
    assert b_legacy.get_config_parser()
    assert b_legacy.get_queue()
    assert b_legacy.get_urllib2()
    pass

def test_logging():
    pass 

def test_math ():    
    from bptbx import b_math
    result = b_math.split_list_to_equal_buckets([1, 2, 3, 4, 5, 6, 7, 8], 3)
    assert result == [[1.0, 2.0, 3.0], [4.0, 5.0], [6.0, 7.0, 8.0]]

def test_pil():
    pass
        
def test_strings ():
    from bptbx import b_strings
    print (b_strings.id_generator())

def test_threading ():
    from bptbx import b_threading
    cpus = b_threading.get_cpus()
    print ('Machine has {0} cpus'.format(cpus))
    pool = b_threading.ThreadPool(cpus)
    for _ in range(0, 10):
        pool.add_task(random_calculation)
    print ('Waiting for jobs to be completed')
    pool.wait_completion()

def test_visual ():
    
    ext_modules = [ 'matplotlib', 'numpy', 'dateutil', 'pyparsing' ]
    success, _ = import_modules_with_check(ext_modules)
    if success:
        from bptbx import b_visual
    else:
        print ('Skipped test for b_visual. Missing external imports.')
        return
    x_axis_dataset = []
    y1 = []
    y2 = []
    for x in range(1, 11):
        x_axis_dataset.append(x)
        y1.append(random.randint(1, 100))
        y2.append(random.randint(1, 100))
    y_axis_datasets = [y1, y2]
    y_axis_datalabels = ['Some data', 'Some other data']
    x_axis_isdatetime = False
    title = 'Test plot'
    x_label = 'Data points'
    y_label = 'Random values'
    fontsize = 9
    fontweight = 'bold'
    
    try:
        b_visual.print_dataset(x_axis_dataset, y_axis_datasets,
                y_axis_datalabels, x_axis_isdatetime, title, x_label,
                y_label, fontsize, fontweight, '%d.%m.%Y\n%H:%M', False)
    except NameError:
        pass

def test_web ():
    success = import_module_with_check('ftputil')
    if success:
        from bptbx import b_web
    else:
        print ('Skipped test for b_web. Missing external imports.')
        return
    content = b_web.download_webpage_to_list('http://www.google.de')
    assert len(content) > 0
    print (content[0])

if __name__ == "__main__":

    test_cmdline()
    test_enum()
    test_iotools()
    test_legacy()
#     test_logging()
#     test_math()
#     test_pil()
#     test_strings()
#     test_threading()
#     test_visual()
#     test_web() 
    test_daemon()
    
    print ('--- all tests have passed.')