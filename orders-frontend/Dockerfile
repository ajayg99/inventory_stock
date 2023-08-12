# Stage 1: Build
FROM node:18-alpine as build
WORKDIR /ord_front
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Production Image
FROM nginx:1.21.0-alpine as production
WORKDIR /inv_front
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /ord_front/build /usr/share/nginx/html
EXPOSE 3001
CMD ["nginx", "-g", "daemon off;"]