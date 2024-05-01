#include "glad/glad.h"

namespace glutils{
	void read_file(const char* filename, char** filetext);
	unsigned int compileShader(GLenum shaderType, const char* src);
	unsigned int createShaderProgram(const char* vtxShaderSrc, const char* fragShaderSrc);
	unsigned int createShaderProgramFiles(const char* vtxFile, const char* fragFile);
}
