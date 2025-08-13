import pytest
from fastapi.testclient import TestClient
from pathlib import Path
from pull_agent.main import app

class TestSubagentAPI:
    """Integration tests for the subagent API endpoints"""
    
    @pytest.fixture
    def client(self):
        """Create a test client for the FastAPI app with lifespan context"""
        with TestClient(app) as test_client:
            yield test_client
    
    @pytest.fixture
    def sample_subagent_content(self):
        """Read the actual CEO subagent file for comparison"""
        subagents_dir = Path(__file__).parent.parent / "subagents"
        ceo_file = subagents_dir / "ceo.md"
        if ceo_file.exists():
            return ceo_file.read_text(encoding="utf-8")
        return None
    
    def test_get_existing_subagent_success(self, client, sample_subagent_content):
        """Test retrieving an existing subagent (CEO)"""
        response = client.get("/api/ceo")
        
        assert response.status_code == 200
        content = response.text
        
        # Check that we get markdown content
        assert len(content) > 0
        
        # Should contain typical markdown content for CEO role
        assert "CEO" in content or "Chief Executive Officer" in content
    
    def test_response_structure_validation(self, client):
        """Test that successful responses return valid markdown content"""
        response = client.get("/api/cto")  # Use CTO as another test case
        
        assert response.status_code == 200
        content = response.text
        
        # Should be substantial markdown content
        assert len(content) > 100
        
        # Should contain CTO-related content
        assert "CTO" in content or "Chief Technology Officer" in content
    
    def test_fuzzy(self, client):
        """Test fuzzy search for executive roles"""
        response = client.get("/api/executive")
        
        assert response.status_code == 200
        content = response.text
        
        # Should contain executive-related content (likely CEO)
        assert "CEO" in content or "executive" in content.lower()
    

    def test_status_endpoint(self, client):
        """Test the status endpoint"""
        response = client.get("/status")
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "up!"