"""
create contact submission model

Revision ID: e312eb5566e5
Revises: 
Create Date: 2017-10-11 17:48:07.358831
"""

from alembic import op
import sqlalchemy as sa


import backend

# revision identifiers, used by Alembic.
revision = 'e312eb5566e5'
down_revision = None
branch_labels = ('site',)
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_submission',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', backend.database.types.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', backend.database.types.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_contact_submission'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact_submission')
    # ### end Alembic commands ###
