CREATE TABLE thoughts (
    id TEXT PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)

CREATE TABLE thoughts_versions (
    id TEXT PRIMARY KEY,
    thought_id TEXT NOT NULL,
    version_number INTEGER NOT NULL,
    content TEXT NOT NULL,
    metadata JSON,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (thought_id) REFERENCES thoughts(id)
)

CREATE TABLE current_thought_versions (
    thought_id TEXT PRIMARY KEY,
    version_id TEXT NOT NULL,
    FOREIGN KEY (thought_id) REFERENCES thoughts(id),
    FOREIGN KEY (version_id) REFERENCES thoughts_versions(id)
)

CREATE INDEX idx_thought_versions ON thoughts_versions (thought_id, version_number);