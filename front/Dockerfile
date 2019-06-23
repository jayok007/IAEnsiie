FROM node:10 as builder
WORKDIR /usr/src/app
COPY . .
RUN npm ci
RUN npm run export

FROM nginx
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /usr/src/app/__sapper__/export /usr/share/nginx/html
