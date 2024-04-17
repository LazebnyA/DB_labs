"""empty message

Revision ID: d16f2f615b0c
Revises: 3bf835066425
Create Date: 2024-04-17 13:21:04.677529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd16f2f615b0c'
down_revision: Union[str, None] = '3bf835066425'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wind_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=255), nullable=True),
    sa.Column('last_updated_epoch', sa.Integer(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.Column('wind_mph', sa.Float(), nullable=True),
    sa.Column('wind_kph', sa.Float(), nullable=True),
    sa.Column('wind_degree', sa.Integer(), nullable=True),
    sa.Column('wind_direction', sa.String(length=3), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('weather_data', sa.Column('record_id', sa.Integer(), nullable=False))
    op.alter_column('weather_data', 'latitude',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'longitude',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'temperature_celsius',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'temperature_fahrenheit',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'pressure_mb',
               existing_type=sa.NUMERIC(precision=6, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'pressure_in',
               existing_type=sa.NUMERIC(precision=6, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'precip_mm',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'precip_in',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'feels_like_celsius',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'feels_like_fahrenheit',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'visibility_km',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'visibility_miles',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'uv_index',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'gust_mph',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'gust_kph',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'air_quality_Carbon_Monoxide',
               existing_type=sa.NUMERIC(precision=6, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'air_quality_Ozone',
               existing_type=sa.NUMERIC(precision=6, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'air_quality_Nitrogen_dioxide',
               existing_type=sa.NUMERIC(precision=6, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'air_quality_Sulphur_dioxide',
               existing_type=sa.NUMERIC(precision=6, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'air_quality_PM25',
               existing_type=sa.NUMERIC(precision=6, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('weather_data', 'air_quality_PM10',
               existing_type=sa.NUMERIC(precision=6, scale=2),
               type_=sa.Float(),
               existing_nullable=True)
    op.drop_column('weather_data', 'wind_degree')
    op.drop_column('weather_data', 'wind_kph')
    op.drop_column('weather_data', 'id')
    op.drop_column('weather_data', 'wind_direction')
    op.drop_column('weather_data', 'wind_mph')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weather_data', sa.Column('wind_mph', sa.NUMERIC(precision=5, scale=2), autoincrement=False, nullable=True))
    op.add_column('weather_data', sa.Column('wind_direction', sa.VARCHAR(length=3), autoincrement=False, nullable=True))
    op.add_column('weather_data', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('weather_data', sa.Column('wind_kph', sa.NUMERIC(precision=5, scale=2), autoincrement=False, nullable=True))
    op.add_column('weather_data', sa.Column('wind_degree', sa.INTEGER(), autoincrement=False, nullable=True))
    op.alter_column('weather_data', 'air_quality_PM10',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=6, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'air_quality_PM25',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=6, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'air_quality_Sulphur_dioxide',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=6, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'air_quality_Nitrogen_dioxide',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=6, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'air_quality_Ozone',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=6, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'air_quality_Carbon_Monoxide',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=6, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'gust_kph',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'gust_mph',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'uv_index',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'visibility_miles',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'visibility_km',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'feels_like_fahrenheit',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'feels_like_celsius',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'precip_in',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'precip_mm',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'pressure_in',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=6, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'pressure_mb',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=6, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'temperature_fahrenheit',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'temperature_celsius',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=5, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'longitude',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=10, scale=2),
               existing_nullable=True)
    op.alter_column('weather_data', 'latitude',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=10, scale=2),
               existing_nullable=True)
    op.drop_column('weather_data', 'record_id')
    op.drop_table('wind_data')
    # ### end Alembic commands ###
