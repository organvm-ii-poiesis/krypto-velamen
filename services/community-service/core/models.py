from django.db import models

class Journal(models.Model):
    """
    A user's personal writing space. 
    Can be 'private' (Substrate) or 'public' (Surface).
    """
    author_handle = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_public = models.BooleanField(default=False)
    
    # "Encoding" Metadata
    mask_type = models.CharField(max_length=50, blank=True)
    affect_cost = models.CharField(max_length=50, blank=True)
    
    # Metabolic Fields
    created_at = models.DateTimeField(auto_now_add=True)
    last_witnessed = models.DateTimeField(auto_now=True)
    decay_level = models.FloatField(default=0.0, help_text="0.0 (Fresh) to 1.0 (Corrupted)")

    def __str__(self):
        return f"{self.author_handle}: {self.title}"

class Thread(models.Model):
    """
    A community discussion linked to a Research Topic.
    """
    topic_id = models.CharField(max_length=50) # e.g. "Topic 26"
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    author_handle = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
