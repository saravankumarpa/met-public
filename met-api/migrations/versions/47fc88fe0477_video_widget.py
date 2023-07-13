"""Add video widget

Revision ID: 47fc88fe0477
Revises: b3b5c66cea4b
Create Date: 2023-07-11 10:44:35.980432

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '47fc88fe0477'
down_revision = 'b3b5c66cea4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('widget_video',
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('widget_id', sa.Integer(), nullable=True),
    sa.Column('engagement_id', sa.Integer(), nullable=True),
    sa.Column('video_url', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_by', sa.String(length=50), nullable=True),
    sa.Column('updated_by', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['engagement_id'], ['engagement.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['widget_id'], ['widget.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    widget_type_table = sa.table('widget_type',
        sa.Column('id', sa.Integer),
        sa.Column('name', sa.String),
        sa.Column('description', sa.String))

    op.bulk_insert(widget_type_table, [
        {'id': 7, 'name': 'Video', 'description': 'Add a link to a hosted video and link preview'}
    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('widget_video')
    
    conn = op.get_bind()

    conn.execute('DELETE FROM widget_type WHERE id=7')
    # ### end Alembic commands ###
