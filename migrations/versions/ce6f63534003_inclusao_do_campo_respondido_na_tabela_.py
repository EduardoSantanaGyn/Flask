"""inclusao do campo respondido na tabela contato

Revision ID: ce6f63534003
Revises: 19a76016bcd2
Create Date: 2025-03-22 00:16:31.527075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce6f63534003'
down_revision = '19a76016bcd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.add_column(sa.Column('respondido', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.drop_column('respondido')

    # ### end Alembic commands ###
