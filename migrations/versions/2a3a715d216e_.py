"""empty message

Revision ID: 2a3a715d216e
Revises: 05ac38d42218
Create Date: 2019-10-26 11:48:38.505097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a3a715d216e'
down_revision = '05ac38d42218'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role_id', sa.Integer(), server_default='0', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'role_id')
    # ### end Alembic commands ###