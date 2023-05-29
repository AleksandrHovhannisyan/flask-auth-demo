"""Remove salt

Revision ID: 389a4e9f5aea
Revises: 3d67f983387d
Create Date: 2023-05-29 11:09:00.778355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '389a4e9f5aea'
down_revision = '3d67f983387d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password_salt')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_salt', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###
