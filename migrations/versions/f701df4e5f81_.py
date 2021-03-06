"""empty message

Revision ID: f701df4e5f81
Revises: 5cdd21789204
Create Date: 2015-12-25 12:44:53.655277

"""

# revision identifiers, used by Alembic.
revision = 'f701df4e5f81'
down_revision = '5cdd21789204'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_image_filename'), 'image', ['filename'], unique=False)
    op.create_index(op.f('ix_image_processed'), 'image', ['processed'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_image_processed'), table_name='image')
    op.drop_index(op.f('ix_image_filename'), table_name='image')
    ### end Alembic commands ###
