"""6

Revision ID: 20db08fd2fcf
Revises: 0af34e8ea563
Create Date: 2024-04-18 10:46:43.807424

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20db08fd2fcf'
down_revision: Union[str, None] = '0af34e8ea563'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wind_data', sa.Column('go_outside', sa.Boolean, nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wind_data', 'go_outside')
    # ### end Alembic commands ###
