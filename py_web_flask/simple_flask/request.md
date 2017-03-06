#####用Flask处理文件上传
- 确保HTML表单中设置enctype="multipart/form-data"属性
- 已上传的文件被储存在内存或文件系统的临时位置；
- 通过{{ request.files }}来访问上传的文件，每个上传的文件都储存在这个ImmutableMultiDict([])字典中；
- request.files.get('...')接收<input type="file" name="..." />上传的文件；
- 或者
    + f = request.files['the_file']
    + f.save('/var/www/uploads/uploaded_file.txt')

通过Werkzeug提供的secure_filename()函数，使用filename属性，可以知道文件上传之前其在客户端系统中的名称
请牢记这个值是 可以伪造的，永远不要信任这个值。
f.save('/var/www/uploads/' + secure_filename(f.filename))

#####使用cookies属性
使用请求对象的set_cookie方法来设置cookies。
cookies 设置在响应对象上。通常只是从视图函数返回字符串，Flask会把它们转换为响应对象。如果你想显式地转换，那么可以使用 make_response() 函数，然后再修改它。
```
@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
```
请求对象的cookies属性是一个包含了客户端传输的所有cookies的字典。

在Flask中，如果能够使用会话，那么就不要直接使用cookies，因为会话比较安全一些。

#####request.json
