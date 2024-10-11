# Define variables for your linters and other settings
PYTHON := python3
LINTERS := flake8 black
SOURCE_FILES := app tests
LINT_OUTPUT := lint_report.txt

# Define the default target
.PHONY: all lint format clean

all: lint

# Lint the source files with specified linters
lint: $(LINTERS)
	@echo "Running linters..."
	@echo "Linting source files..." > $(LINT_OUTPUT)
	@for linter in $(LINTERS); do \
		echo "Running $$linter..."; \
		$$linter $(SOURCE_FILES) >> $(LINT_OUTPUT) 2>&1; \
	done
	@echo "Linting completed. See $(LINT_OUTPUT) for details."

# Format the code with black
format:
	@echo "Formatting code with Black..."
	@black $(SOURCE_FILES)

# Clean any linting output files
clean:
	@echo "Cleaning up lint report..."
	@rm -f $(LINT_OUTPUT)

# Install the necessary packages
install:
	@echo "Installing required packages..."
	@pip install flake8 black
