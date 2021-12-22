import pandas as pd
import dataframe_image as dfi

df = pd.read_excel("file.xlsx")

# 提取部门简写
df["发起人部门"] = (df["发起人部门"].map(lambda s : s.split('-')[-1])).map(lambda s : s[2:4] if "部" in s else s[-3:] if "队" in s else s)
# 部门、姓名重命名
df.rename(columns={'发起人姓名': '姓名', '发起人部门': '部门'}, inplace=True)

result = df[["部门","姓名","请假类型", "开始时间", "结束时间", "时长"]]
result.index = result.index + 1  # 设置索引号从 1 开始

result.to_excel("请假情况.xlsx", index=False)
result.to_html("html.html")

dfi.export(obj=result, filename='请假情况.jpg', fontsize=30)