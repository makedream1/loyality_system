from django_clickhouse import migrations
from statistic.clickhouse_models import Statistic


class Migration(migrations.Migration):
    operations = [
        migrations.CreateTable(Statistic)
    ]