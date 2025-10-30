FROM agrigorev/zoomcamp-model:2025
# add your stuff here

# Copy the 'uv' and 'uvx' executables from the latest uv image into /bin/ in this image
# 'uv' is a fast Python package installer and environment manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Add the virtual environment's bin directory to the PATH so Python tools work globally
ENV PATH="/code/.venv/bin:$PATH"

COPY ".python-version" "pyproject.toml" "uv.lock" "./"

# Install dependencies 
RUN uv sync --locked

COPY "predict.py" "./"

EXPOSE 9696

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]