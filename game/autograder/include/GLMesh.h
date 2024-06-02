#include "glad/glad.h"
namespace glutils{

struct GLMesh{
	GLMesh();	
	~GLMesh();
	void buffer(float* verts, unsigned int verts_size, unsigned int* indices, unsigned int ibo_size);
	void draw();
	GLenum drawMode;
	private:
		unsigned int vbo, ibo;
		unsigned int vao;
		unsigned int ibo_size;

};

}
