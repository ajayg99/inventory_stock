FROM node:18-alpine

WORKDIR /inv_front

COPY ./package.json /inv_front

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]