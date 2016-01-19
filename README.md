# python-bos-client

python版本百度BOS对象存储客户端.

BCE-CLI没提供批量删除功能，所以用sdk加上了“批量删除”。

## Conf

- conf/conf.py

```
bos_host = "bj.bcebos.com"
access_key_id = "ak"
secret_access_key = "sk"
```

复制一份conf.sample.py文件并改名为conf.py，修改 ak & sk & host保存即可

## Usage

- 通用方法

```
python client.py {del || dels || list} {bucket_name} {prefix || key_name}
```

- 批量删除

```
python client.py dels bucket_name prefix 
```

- 单个删除

```
python client.py del bucket_name key_name 
```

- 获取列表

```
python client.py list bucket_name prefix 
```

## TOC

- 批量上传（带目录结构）
- 其他功能（想到再加）

## License

The MIT License (MIT)

Copyright (c) 2015 Magic Term Libraries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.