# Title

Human Approval for Alert Summaries

## Status

Accepted

## Context

An incorrect or misleading automated summary could cause the on-call engineer to under-react or over-react to a real incident. A few minutes of approval delay costs much less than a bad summary during an active incident.

## Decision

The n8n alert-summary workflow routes each generated summary to a human for approval before it is sent to the on-call channel, instead of sending it automatically.

## Consequences

Delivery is slower and depends on someone being available to approve.