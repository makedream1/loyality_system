from django_clickhouse.clickhouse_models import ClickHouseModel
from django_clickhouse.engines import MergeTree
from infi.clickhouse_orm import fields
from infi.clickhouse_orm.funcs import F


class Statistic(ClickHouseModel):

    balance = fields.UInt64Field(default=0)
    created_date = fields.DateTime64Field(default=F.now())

    engine = MergeTree('created_date', ('created_date',))
