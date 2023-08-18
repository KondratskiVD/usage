#     Copyright 2020 getcarrier.io
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String, Float
from sqlalchemy.dialects.postgresql import JSON

from tools import db, db_tools, rpc_tools


class UsageAPI(db_tools.AbstractBaseMixin, db.Base, rpc_tools.RpcMixin):
    __tablename__ = "usage_api"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, unique=False, nullable=True)
    mode = Column(String(64), unique=False, nullable=True)
    user = Column(String(128), unique=False, nullable=True)
    endpoint = Column(String(256), unique=False, nullable=True)
    method = Column(String(16), unique=False, nullable=True)
    date = Column(DateTime, default=datetime.utcnow)
    view_args = Column(JSON, unique=False, nullable=True)
    query_params = Column(JSON, unique=False, nullable=True)
    json = Column(JSON, unique=False, nullable=True)
    files = Column(JSON, unique=False, nullable=True)
    run_time = Column(Float, unique=False, default=0)
    status_code = Column(Integer, unique=False, nullable=True)
