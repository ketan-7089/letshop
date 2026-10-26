# ==========================================
# Stage 1: Build Stage (Vite Frontend Bundle)
# ==========================================
FROM node:20-alpine AS builder

WORKDIR /app

# Copy dependency manifests
COPY package*.json ./

# Install all dependencies including devDependencies for Vite compilation
RUN npm install

# Copy application source code
COPY . .

# Build React 18 production bundle into /dist
RUN npm run build

# ==========================================
# Stage 2: Production Runtime Stage
# ==========================================
FROM node:20-alpine AS runner

WORKDIR /app

# Set production environment variables
ENV NODE_ENV=production
ENV PORT=3000

# Install curl/wget for container health checks
RUN apk add --no-cache wget

# Copy package manifests and install only production dependencies
COPY package*.json ./
RUN npm install --omit=dev

# Copy compiled static assets from builder stage
COPY --from=builder /app/dist ./dist

# Copy backend server code and routes
COPY --from=builder /app/app.js ./app.js
COPY --from=builder /app/server ./server
COPY --from=builder /app/public ./public

# Expose HTTP application port
EXPOSE 3000

# Docker Healthcheck targeting the MCA /health endpoint
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD wget -qO- http://localhost:3000/health || exit 1

# Start Node.js Express server
CMD ["node", "app.js"]
