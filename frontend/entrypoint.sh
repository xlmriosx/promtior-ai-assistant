#!/bin/sh

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

log "Starting frontend container..."

if ! command -v envsubst >/dev/null 2>&1; then
    log "ERROR: envsubst not found. Installing gettext..."
    apk add --no-cache gettext
fi

log "Generating runtime configuration..."
envsubst < /usr/share/nginx/html/config.template.js > /usr/share/nginx/html/config.js

log "Generated config:"
cat /usr/share/nginx/html/config.js

rm -f /usr/share/nginx/html/config.template.js

log "Starting nginx..."
exec nginx -g 'daemon off;'