"""group member add  FK

Revision ID: ad5ead2aa5f4
Revises: 6551900c3104
Create Date: 2023-03-10 09:21:50.863131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad5ead2aa5f4'
down_revision = '6551900c3104'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('group_member', sa.Column('invited_by', sa.UUID(), nullable=True))
    op.create_foreign_key(None, 'group_member', 'user', ['invited_by'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'group_member', type_='foreignkey')
    op.drop_column('group_member', 'invited_by')
    # ### end Alembic commands ###
