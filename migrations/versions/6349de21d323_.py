"""empty message

Revision ID: 6349de21d323
Revises: 4baef864e579
Create Date: 2024-01-31 20:23:22.521398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6349de21d323'
down_revision = '4baef864e579'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stock_take_inventory', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_barcode', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('insert_date', sa.DateTime(), nullable=True))
        batch_op.create_foreign_key('stock_take_inventory', 'stock_take', ['stock_take_id'], ['id'])
        batch_op.drop_column('product_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stock_take_inventory', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('insert_date')
        batch_op.drop_column('product_barcode')

    # ### end Alembic commands ###