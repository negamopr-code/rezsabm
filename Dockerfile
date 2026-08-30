FROM node:20-bookworm-slim
RUN apt-get update \
 && apt-get install -y --no-install-recommends python3 python3-pil fonts-dejavu-core curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
ENV PORT=8112
EXPOSE 8112
CMD ["node", "server.js"]
