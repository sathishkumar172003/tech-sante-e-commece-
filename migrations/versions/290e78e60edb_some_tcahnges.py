"""some tcahnges

Revision ID: 290e78e60edb
Revises: 2590c9134a26
Create Date: 2023-01-03 13:22:18.191284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '290e78e60edb'
down_revision = '2590c9134a26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customer_order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('carts_id', sa.Integer(), nullable=False))
        batch_op.alter_column('ordered_date',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('deliver_date',
               existing_type=sa.DATETIME(),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.create_foreign_key(None, 'cart', ['carts_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customer_order', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('deliver_date',
               existing_type=sa.String(length=50),
               type_=sa.DATETIME(),
               existing_nullable=False)
        batch_op.alter_column('ordered_date',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.drop_column('carts_id')
        batch_op.drop_column('status')

    # ### end Alembic commands ###