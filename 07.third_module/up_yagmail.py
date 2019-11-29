import yagmail


yag = yagmail.SMTP(user='****', password='****', host='smtp.qq.com')
contents = [
    "各位同学:",
    "  ", "见信好! 我是...",
    "事件或申请",
    "..."
]
yag.send(to='bavduer@163.com', subject='yagmail test',
         contents=contents, attachments='instructure.txt', cc='853942672@qq.com')
# attachments: 发送附件
# cc: 抄送

# 收件人: 运维负责人;当天值班人员;(机房值守人员;)
# 抄送: 老板(运维总监/CTO);运维部;开发组;开发组负责人;
# 添加的附件: Excel.xlsx; .xls;


