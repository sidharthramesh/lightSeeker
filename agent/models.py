from django.db import models
import numpy as np
# Create your models here.

def randPosition(scale=100):
    return scale * np.random.rand()

def randAngle():
    return 2*np.pi * np.random.rand()

class Agent(models.Model):
    positionX = models.FloatField(default=randPosition)
    positionY = models.FloatField(default=randPosition)
    size = models.FloatField(default=10)
    angle = models.FloatField(default=randAngle)
    speed = models.FloatField(default=0.5)
    torque = models.FloatField(default=0.05)

    def position(self):
        return np.array([self.positionX, self.positionY])

    def sensorPosition(self):
        # a = self.size / np.sqrt(3)
        a =0.5
        return self.position() + a* (self.size * np.array([np.cos(self.angle), np.sin(self.angle)]))

    def step(self, left, right):
        if left and right:
            movementX, movementY = self.speed* np.array([np.cos(self.angle), np.sin(self.angle)])
            self.positionX += movementX
            self.positionY += movementY
        if left:
            self.angle -= self.torque * np.pi
        if right:
            self.angle += self.torque * np.pi
        return self

class Light(models.Model):
    positionX = models.FloatField(default=randPosition)
    positionY = models.FloatField(default=randPosition)
    brightness = models.FloatField(default=48)

    def position(self):
        return np.array([self.positionX, self.positionY])

class Graph(models.Model):
    agent = models.ForeignKey(Agent, models.CASCADE, "graph")
    light = models.ForeignKey(Light, models.CASCADE, "graph")

    def distance(self):
        distance = self.agent.sensorPosition() - self.light.position()
        return np.sqrt(np.sum((distance)**2))

    def sensor(self):
        scale = self.light.brightness
        lightDecay = 2*scale/(1+np.exp(0.069*self.distance()))
        return lightDecay
    
    def step(self, left, right):
        self.agent.step(left, right)
        self.agent.save()