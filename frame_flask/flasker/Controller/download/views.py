# encoding=utf-8
from flask import request, render_template, jsonify
from flask.views import MethodView
from DataMap.Corp.corp import DownloadCenter
from Common.common_utils import CommonUtils

class DownloadCenterAction(MethodView):
    def get(self):
        pageindex = request.args.get('pindex', 1, type=int)
        pagesize = request.args.get('psize', 50, type=int)
        data = DownloadCenter.select().order_by(DownloadCenter.upload_at.desc()).paginate(pageindex, pagesize)
        count = DownloadCenter.select().order_by(DownloadCenter.upload_at.desc()).count()
        pagecount = count / pagesize + (1 if (count % pagesize) > 0 else 0)
        for i in data:
            i.upload_at = CommonUtils.unixtime_to_str(i.upload_at)
            i.link = str(i.link)
        return render_template('download/download_center.html',
                               data=data,
                               pagecount=pagecount,
                               pagesize=pagesize,
                               pageindex=pageindex)

    def post(self):
        if request.form.get("mark") == "111":
            upload_at = CommonUtils.get_unixtime()
            file_name = request.form.get('file_name', '').strip()
            link = request.form.get('link', '').strip()
            file_type = link.split('.')[-1]
            DownloadCenter.create(upload_at=upload_at,file_name=file_name,link=link,file_type=file_type)
            return jsonify({"success": "ok"})
        if request.form.get("mark") == "222":
            ids = request.form.getlist('ids[]')
            for id in ids:
                DownloadCenter.delete().where(DownloadCenter.id == id).execute()
            return "ok"