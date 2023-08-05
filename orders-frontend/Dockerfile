FROM node:18-alpine

WORKDIR /ord_front

COPY ./package.json /ord_front

RUN npm install

COPY . .

EXPOSE 3001

CMD ["npm", "start"]