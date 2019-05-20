#!/usr/bin/env bash

echo 'Creating application user and db'

mongo ${APP_MONGO_DB} \
        -u ${MONGO_ROOT_USERNAME} \
        -p ${MONGO_ROOT_PASSWORD} \
        --authenticationDatabase admin \
        --eval "db.createUser({user: '${APP_MONGO_USERNAME}', pwd: '${APP_MONGO_PASSWORD}', roles:[{role:'dbOwner', db: '${APP_MONGO_DB}'}]});"

echo 'Finished creating application user and db'
