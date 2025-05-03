# Talabat E-Commerce Project

## Project Architecture

This is a microservices-based e-commerce application built using .NET 6 and Angular, containerized with Docker.

### Components

1. **Backend API (.NET 6)**
   - Clean Architecture pattern
   - RESTful API endpoints
   - Entity Framework Core for data access
   - Identity for authentication
   - Redis for caching

2. **Frontend (Angular)**
   - Modern SPA application
   - Responsive design
   - State management
   - REST API integration

3. **Database**
   - SQL Server 2022
   - Two databases:
     - TalabatProjectDB (main application)
     - TalabatIdentityDB (authentication)

4. **Caching**
   - Redis 7.0.11
   - Used for performance optimization

5. **Reverse Proxy**
   - Nginx
   - Handles routing and load balancing
   - SSL termination

### Infrastructure

- **Docker Containers:**
  - API Service
  - Angular Client
  - Nginx Reverse Proxy
  - SQL Server
  - Redis Cache

- **Docker Compose Configuration:**
  - Service orchestration
  - Environment configuration
  - Volume management
  - Health monitoring

### Getting Started

1. **Prerequisites:**
   - Docker Desktop
   - .NET 6 SDK (for development)
   - Node.js (for development)

2. **Running the Application:**
   ```bash
   docker-compose up -d
   ```

3. **Access Points:**
   - Web Application: http://localhost:8080
   - API: http://localhost:8080/api
   - SQL Server: localhost:1433
   - Redis: localhost:6379

### Development

- Backend located in `./TalabatProject`
- Frontend located in `./client`
- Nginx configuration in `./nginx`

### Security Notes

- Secure passwords should be used in production
- SSL certificates should be configured
- Environment variables should be properly managed
- Proper network security rules should be implemented

### Monitoring

- Health checks implemented for all services
- Container logs available via Docker
- Database monitoring through SQL Server tools
- Redis monitoring through Redis CLI

### Data Persistence

- SQL Server data persisted in named volume: `sqldata`
- Redis data persisted in named volume: `redisdata`