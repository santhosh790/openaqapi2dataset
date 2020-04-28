import openaq
import dataset

aq = openaq.OpenAQ()
ds = dataset.DSCreater()
latest = aq.get_latest()
ds.
