# 说明文档
------
## 目录结构和文件说明
- markone_server
    - settings.py django主配置
    - urls.py django主路由文件
    - env.py 测试环境和线上环境分开配置
- env 干净的虚拟开发环境，规避包版本冲突
- data json文件，开发使用的模拟数据
- deploy 部署所需的配置文件
- pages HTML静态页面，前端开发提供给后端模版使用的页面
- static
    - app js文件，一般对应pages里的html文件
    - fonts 字体文件
    - images 图片
    - lib 公用的工具类库文件
    - modules 模块或者组件文件，html／js
    - scss 样式文件
- templates django 模板文件，模板语言mako, django-mako
- api 对外接口目录
- app 主程序

## 分支介绍
- `online`分支 线上版本
- `master`分支 主分支，包含了已确定没问题的代码
- `develop`分支 测试环境版本

## 开发过程
- 从`master`切独立分支，然后合并到master，最终online上线
- merge之前，`fetch`一下分支，`git rebase [origin/branch]`

## 代码风格
- simple is best
- 尽量使用单引号字符串
- 尽量不要用#号注释代码，不用的代码就删掉
- 未完成模块或未使用的类或方法，不提交
- 方法说明看眼神，领悟神队友

## 类库包引用与方法函数
- 库引用顺序，每种包之间隔一个空行：
    ```
    系统内置包
    第三方包
    项目自建包
    ```
- 以check_开头的函数，如果检查通过则不返回任何东西，如果检查失败则抛出异常。

## 自动测试和代码风格检查
> Note:
>1. 提交代码前需要自行完成单元测试以及代码风格检查
>1. flask8代码检查较严格，标点、断行100字符、类库未使用都会失败
>1. 单元测试和flask8代码检查参考Makefile中build和test部分

    ```
    flake8 [django_app] --show-source --statistics --count
    python manage.py test [django_app]
    ```

## 部署
------
## 前端
- 前端使用的库：
- 前端项目要求：web站项目暂定要求支持IE9+
- 前端使用库的文档：

------

### 本地部署
- ubuntu需要的步骤
    ```
    sudo apt-get update
    sudo apt-get install libfreetype6-dev pkg-config libmysqld-dev libpng12-dev libblas-dev liblapack-dev
    sudo apt-get install python-dev
    sudo apt-get install mysql-server
    sudo apt-get install ipython
    sudo apt-get install python-lxml python-pip
    sudo apt-get install tree
    # 中文支持
    sudo locale-gen zh_CN.UTF-8
    sudo apt-get install `check-language-support -l zh-hans`
    ```

- 安装mysql, brew安装会自动添加mysql的环境变量，如果后面pip install报了mysql的错误，一般是环境变量问题
    ```
    brew install mysql
    pip install virtualenv
    ```

- 先cd到项目目录，创建Python虚拟环境项目
    ```
    virtualenv env
    ```

- 激活虚拟环境+migrate数据库
    ```
    source env/bin/activate
    python manage.py migrate
    ```

- 安装项目需要的模块
    ```
    pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
    ```

- 创建日志目录和文件
    ```
    mkdir logs && touch logs/std-err.log
    ```

- 数据库方案二选一，功能和缓存加速使用redis
    - 一，开发阶段为方便使用sqlite3
    - 二，使用测试mysql和redis，修改hosts

        ```
        127.0.0.1   mysql.markone_server.info
        127.0.0.1   redis.markone_server.info
        ```

    - 三，mysql本地部署，如果需要使用本地数据库，数据库文件可以找同事要一份导入到本地；redis本地部署等待补充
        - 修改数据库支持utf8，然后restart
           ```
           vim /etc/mysql/my.cnf
           [client]
           default-character-set=utf8

           [mysqld]
           collation-server = utf8_unicode_ci
           character-set-server = utf8

           [mysql]
           default-character-set=utf8
           ```

        - 修改settings.py后，git管理有问题，暂时解决方案是把配置中数据库地址在host中指向127.0.0.1

            ```
            127.0.0.1	mysql.markone_server.info
            ```

        - 把本地的数据库的用户名和密码和数据库名设置成配置中

            ```
            mysql -u root -p

            CREATE USER 'markone_server'@'localhost' IDENTIFIED BY 'password';

            GRANT ALL ON *.* TO 'markone_server'@'localhost';

            flush privileges;

            exit;

            mysql -u markone_server -p

            create database markone_server;
            ```

- 生成前端资源文件
    ```
    ```

- 运行服务

    ```
    source env/bin/activate
    python manage.py runserver 0.0.0.0:11112
    ```

- 本地账号登录

    ```
    http://0.0.0.0:11112/admin
    ```

### 线上部署
- ** aliyun部署默认root权限，目录结构以/root/开头，需要根据服务器情况，注意配置deploy里的directory
- ** aliyun默认开放了ssh端口，但是对外访问需要在【安全组规则】中设置【出方向】
- 线上运行
    ```
    supervisorctl
    root@iZ2ze6z10ww5vbimxty1olZ:~# supervisorctl
    markone_server                   RUNNING    pid 10984, uptime 0:09:30
    celery_beat                      RUNNING    pid 10967, uptime 0:09:31
    celery_worker                    RUNNING    pid 10977, uptime 0:09:30
    flower                           RUNNING    pid 10968, uptime 0:09:31
    supervisor> restart all
    ```
    或者
    ```
    cd /root/markone_server
    source env/bin/activate
    make restart
    ```
- 线上定时任务、异步任务监测使用flower
    {部署服务的ip}:5555,账号密码markone_server