# pattern-standards: docs-repo verb subset (OMNI-CORE 2, mirroring spec-standards)

VOICE ?= $(HOME)/dev/src/standards/scripts/voice-lint.py

.PHONY: help lint check eval ci

help:
	@echo "lint      - voice-lint --strict over all Markdown (SKIP when the standards canon is absent)"
	@echo "check     - scripts/check-canon.py: ID resolution, catalog mirror, node sets, count claims"
	@echo "ci        - lint + check (the gate CI mirrors; AGENTS.md rule 9)"

lint:
	@if [ -f "$(VOICE)" ]; then \
		python3 $(VOICE) --strict .; \
	else \
		echo "SKIP: voice-lint not found at $(VOICE)"; \
	fi

check:
	@python3 scripts/check-canon.py

eval:
	@python3 scripts/route.py --eval

ci: lint check eval
