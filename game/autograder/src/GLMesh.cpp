#include "GLMesh.h"

namespace glutils{

	GLMesh::GLMesh()
	{
		glGenBuffers(1, &vbo);
		glGenBuffers(1, &ibo);
		glGenVertexArrays(1, &vao);
		glBindVertexArray(vao);
		glBindBuffer(GL_ARRAY_BUFFER, vbo);
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibo);
		glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3*sizeof(float), (void*)0);
		glEnableVertexAttribArray(0);
		glBindVertexArray(0);
		drawMode = GL_TRIANGLES;
	}

	GLMesh::~GLMesh()
	{

	}

	void GLMesh::buffer(float * verts, unsigned int verts_size, unsigned int *indices, unsigned int indices_size)
	{
		glBindBuffer(GL_ARRAY_BUFFER, vbo);
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibo);
		glBufferData(GL_ARRAY_BUFFER, verts_size*sizeof(float), verts, GL_STATIC_DRAW);
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_size*sizeof(unsigned int), indices, GL_STATIC_DRAW);
		ibo_size = indices_size;
	}

	void GLMesh::draw()
	{
		glBindVertexArray(vao);
		glDrawElements(drawMode, ibo_size, GL_UNSIGNED_INT, 0);
		glBindVertexArray(0);

	}
}
