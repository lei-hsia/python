 终于能跑pytest了
 
 debug过程: 
 
 #### 1. Mac上安装```pony```, ```pytest```: ```pytest``` error: 
 ```
 test_sql.py EEEEEEEE                                                     [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_select_top _______________________

item = <Function test_select_top>

    def pytest_runtest_setup(item):
    
>       remote_data = item.get_marker('remote_data')
E       AttributeError: 'Function' object has no attribute 'get_marker'

/Applications/anaconda3/lib/python3.6/site-packages/pytest_remotedata/plugin.py:64: AttributeError
_____________________ ERROR at setup of test_select_values _____________________

 ```
 
#### 2. ```pytest``` remotedata的原因; Google找到github page:

```conda install pytest; pip install pytest-remotedata>=0.3.1```应该能解决; 这两个跑出来没有问题;

```pytest test_sql.py```:出现bug: 

```
xcrun: error: active developer path (“/Applications/Xcode.app/Contents/Developer”) does not exist
```
估计是之前写C++安装了Xcode后来删掉带来的default bash profile的问题, 

解决办法: ```$ sudo xcode-select --reset```. [详情](https://stackoverflow.com/questions/35009531/xcrun-error-active-developer-path-applications-xcode-app-contents-developer)

#### 3. ```pytest test_sql.py```:出现1中的bug; 没办法了; Mac上的代码转移到Ubuntu上(CentOS backup);

#### 4. Ubuntu: 

```
文件系统        容量  已用  可用 已用% 挂载点
udev            972M     0  972M    0% /dev
tmpfs           199M   22M  177M   11% /run
/dev/sda1        21G   20G  4M   100% /   <--------------- You must be fucking kidding
tmpfs           992M   15M  977M    2% /dev/shm
tmpfs           5.0M  4.0K  5.0M    1% /run/lock
tmpfs           992M     0  992M    0% /sys/fs/cgroup
tmpfs           199M  112K  199M    1% /run/user/1000

```

#### 5. ```sda1```是disk分区里面的最大盘，要clear一些; 

查找到```ncdu```这个解析整个Linux中所有文件按照size排序的结果; clear;

#### 6. PyCharm过期

查找lanyu大佬的破解方法: terminated; 找别的破解方法: 花了1个小时破解了;

#### 7. 直接从Mac的代码移植到ubuntu中, PyCharm的terminal运行，居然还是显示的Mac的文件路径，虽然是在Linux中;

原因: 因为这个code的repo是直接```git clone SSH/HTTPS_xxx```得到的, 这个repo是**PRIVATE**,所以有metadata粘滞，对应的file全部是clone
写死的，路径也不会改变。

办法: 从Ubuntu host直接```git clone```.

问题: 我自己的github并不认识Ubuntu宿主这个host，必须要添加public key;

办法: 在ubuntu的默认```id_rsa.pub```文件中找到公钥，添加到github中; [详情](https://github.com/lei-hsia/python/blob/master/Greenwich_St_A_Praktitum/1009_id_rsa_key.md)

#### 8. Ubuntu中的terminal运行路径改对了，变成了ubuntu的路径, 还是安装```pony```和```pytest```;

```
===================================================================================== ERRORS =====================================================================================
__________________________________________________________________________ ERROR collecting test_sql.py __________________________________________________________________________
ImportError while importing test module '/home/python/Desktop/gsa_code/object-service/tests/test_sql.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
test_sql.py:4: in <module>
    from objsvc import DbScope, JoinType
../objsvc/__init__.py:1: in <module>
    from .dbscope import DbScope, bind_func
../objsvc/dbscope.py:6: in <module>
    from pony.orm.decompiling import decompile
../../../../anaconda3/lib/python3.6/site-packages/pony/orm/__init__.py:3: in <module>
    from pony.orm.core import *
../../../../anaconda3/lib/python3.6/site-packages/pony/orm/core.py:18: in <module>
    from pony.thirdparty.compiler import ast, parse
../../../../anaconda3/lib/python3.6/site-packages/pony/thirdparty/compiler/__init__.py:26: in <module>
    from .pycodegen import compile, compileFile
../../../../anaconda3/lib/python3.6/site-packages/pony/thirdparty/compiler/pycodegen.py:19: in <module>
    import pony.utils
E   ModuleNotFoundError: No module named 'pony.utils'
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
============================================================================ 1 error in 0.66 seconds =============================================================================
python@ubuntu:~/Desktop/gsa_code/object-service/tests$ conda install pony
Solving environment: failed

# >>>>>>>>>>>>>>>>>>>>>> ERROR REPORT <<<<<<<<<<<<<<<<<<<<<<

    Traceback (most recent call last):
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/core/repodata.py", line 202, in _load
        mod_etag_headers.get('_mod'))
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/core/repodata.py", line 408, in fetch_repodata_remote_request
        raise Response304ContentUnchanged()
    conda.core.repodata.Response304ContentUnchanged
    
    During handling of the above exception, another exception occurred:
    
    Traceback (most recent call last):
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/exceptions.py", line 789, in __call__
        return func(*args, **kwargs)
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/cli/main.py", line 78, in _main
        exit_code = do_call(args, p)
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/cli/conda_argparse.py", line 77, in do_call
        exit_code = getattr(module, func_name)(args, parser)
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/cli/main_install.py", line 11, in execute
        install(args, parser, 'install')
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/cli/install.py", line 236, in install
        force_reinstall=context.force,
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/core/solve.py", line 504, in solve_for_transaction
        force_remove, force_reinstall)
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/core/solve.py", line 437, in solve_for_diff
        final_precs = self.solve_final_state(deps_modifier, prune, ignore_pinned, force_remove)
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/core/solve.py", line 178, in solve_final_state
        index, r = self._prepare(prepared_specs)
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/core/solve.py", line 560, in _prepare
        self.subdirs, prepared_specs)
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/core/index.py", line 213, in get_reduced_index
        new_records = query_all(spec)
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/core/index.py", line 186, in query_all
        return tuple(concat(future.result() for future in as_completed(futures)))
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/core/repodata.py", line 90, in query
        self.load()
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/core/repodata.py", line 134, in load
        _internal_state = self._load()
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/core/repodata.py", line 208, in _load
        mod_etag_headers.get('_mod'))
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/core/repodata.py", line 255, in _read_local_repdata
        _internal_state = self._process_raw_repodata_str(raw_repodata_str)
      File "/home/python/anaconda3/lib/python3.6/site-packages/conda/core/repodata.py", line 292, in _process_raw_repodata_str
        json_obj = json.loads(raw_repodata_str or '{}')
      File "/home/python/anaconda3/lib/python3.6/json/__init__.py", line 354, in loads
        return _default_decoder.decode(s)
      File "/home/python/anaconda3/lib/python3.6/json/decoder.py", line 339, in decode
        obj, end = self.raw_decode(s, idx=_w(s, 0).end())
      File "/home/python/anaconda3/lib/python3.6/json/decoder.py", line 355, in raw_decode
        obj, end = self.scan_once(s, idx)
    json.decoder.JSONDecodeError: Expecting ',' delimiter: line 44022 column 6 (char 1347584)

`$ /home/python/anaconda3/bin/conda install pony`

  environment variables:
                 CIO_TEST=<not set>
          COMPIZ_BIN_PATH=/usr/bin/
               CONDA_ROOT=/home/python/anaconda3
            DEFAULTS_PATH=/usr/share/gconf/ubuntu.default.path
          LD_LIBRARY_PATH=/opt/pycharm-2016.3.1/bin:
           MANDATORY_PATH=/usr/share/gconf/ubuntu.mandatory.path
                  NLSPATH=/usr/dt/lib/nls/msg/%L/%N.cat
                     PATH=/home/python/anaconda3/bin:/home/python/anaconda3/bin:/usr/local/sbin:
                          /usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/gam
                          es:/snap/bin:/home/python/Downloads/node-v6.1.0-linux-x64/bin:/home/py
                          thon/Downloads/node-v6.1.0-linux-x64/bin
               PYTHONPATH=.
       REQUESTS_CA_BUNDLE=<not set>
            SSL_CERT_FILE=<not set>
            XDG_SEAT_PATH=/org/freedesktop/DisplayManager/Seat0
         XDG_SESSION_PATH=/org/freedesktop/DisplayManager/Session0
          XFILESEARCHPATH=/usr/dt/app-defaults/%L/Dt

     active environment : None
       user config file : /home/python/.condarc

```

是因为当前 virtualenv 中的dependency缺失.

办法: 开一个新的virtualenv, 重新安装所有包。另外，因为当前的环境是在```conda```下，不是```pip```, 用```pip```还会出现pip源的问题, 

```
python@ubuntu:~/Desktop/gsa_code/object-service/tests$ conda info --env
# conda environments:
#
base                  *  /home/python/anaconda3
ml5                      /home/python/anaconda3/envs/ml5

```

所以用```conda```开新的虚拟环境，不用```pip```

#### 9. 最后安装，开新的环境

```
conda create -n py37 python=3.7 astor pyodbc
source activate py37
pip install pony
```

```pyodbc```类似java的```jdbc```, ```pony```和```astor```都是ORM的包

至此， pytest终于能run了
