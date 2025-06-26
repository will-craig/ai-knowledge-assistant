FROM node:18-slim

RUN apt-get update && apt-get upgrade -y && apt-get clean

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
