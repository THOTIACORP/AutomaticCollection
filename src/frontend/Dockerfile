FROM node:18-alpine
WORKDIR /usr/src/app
COPY next-app/package.json .
RUN npm install
COPY next-app ./
CMD ["npm","run","dev"]
