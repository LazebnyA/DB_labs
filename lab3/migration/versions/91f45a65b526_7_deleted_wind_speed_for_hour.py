"""7_deleted wind speed for hour

Revision ID: 91f45a65b526
Revises: 20db08fd2fcf
Create Date: 2024-04-18 11:00:51.536481

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '91f45a65b526'
down_revision: Union[str, None] = '20db08fd2fcf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wind_data', 'wind_mph')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wind_data', sa.Column('wind_mph', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    # ### end Alembic commands ###