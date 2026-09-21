#!/usr/bin/env bash
# ==============================================================================
# LetShop EC2 Deployment Script
# Deploys built Vite frontend (dist.tar.gz) to Nginx web root on AWS EC2
# ==============================================================================

set -euo pipefail

TARBALL="${1:-/tmp/dist.tar.gz}"
TARGET_DIR="${2:-/var/www/letshop}"

echo "=========================================="
echo "Starting LetShop Deployment on EC2"
echo "Target directory: ${TARGET_DIR}"
echo "Archive file:     ${TARBALL}"
echo "=========================================="

# 1. Verify that the build archive exists
if [ ! -f "${TARBALL}" ]; then
    echo "ERROR: Build archive ${TARBALL} not found!" >&2
    exit 1
fi

# 2. Ensure target directory exists
echo "Creating/verifying target directory: ${TARGET_DIR}..."
sudo mkdir -p "${TARGET_DIR}"

# 3. Clean old files in target directory to prevent orphaned files
echo "Cleaning existing application files in ${TARGET_DIR}..."
sudo rm -rf "${TARGET_DIR:?}"/*

# 4. Extract new build archive into target directory
echo "Extracting ${TARBALL} into ${TARGET_DIR}..."
sudo tar -xzf "${TARBALL}" -C "${TARGET_DIR}"

# 5. Set proper web server ownership and permissions
echo "Setting permissions for www-data..."
sudo chown -R www-data:www-data "${TARGET_DIR}"
sudo find "${TARGET_DIR}" -type d -exec sudo chmod 755 {} +
sudo find "${TARGET_DIR}" -type f -exec sudo chmod 644 {} +

# 6. Clean up temporary archive
echo "Cleaning up temporary files..."
rm -f "${TARBALL}"

# 7. Reload Nginx to ensure new files and caching headers are active
echo "Reloading Nginx web server..."
if command -v systemctl >/dev/null 2>&1; then
    sudo systemctl reload nginx
    echo "Nginx reloaded successfully."
else
    sudo service nginx reload || true
fi

echo "=========================================="
echo "LetShop deployment completed successfully!"
echo "=========================================="
