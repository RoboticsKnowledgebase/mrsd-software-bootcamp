#include <iostream>
#include <fstream>
#include "glutils.h"

namespace glutils{

unsigned int compileShader(GLenum shaderType, const char* src)
{
	unsigned int shader;
	shader = glCreateShader(shaderType);
	glShaderSource(shader, 1, &src, NULL);
	glCompileShader(shader);
	int success;
	char log[512];
	glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
	if(!success)
	{
		glGetShaderInfoLog(shader, 512, NULL, log);		
		std::cout << "compilation failed:" << log << std::endl;
	}
	return shader;
}

void read_file(const char* filename, char** filetext)
{
	std::ifstream fstream(filename, std::ios::in);
	if(fstream){
		fstream.seekg(0, fstream.end);
		unsigned long length = (unsigned long)fstream.tellg();
		fstream.seekg(0, fstream.beg);
		*filetext = new char[length+1];
		fstream.read(*filetext, length);
		fstream.close();
		(*filetext)[length] = '\0';
	}
}

unsigned int createShaderProgram(const char* vtxShaderSrc, const char* fragShaderSrc)
{
	unsigned int fShader = compileShader(GL_FRAGMENT_SHADER, fragShaderSrc);
	unsigned int vShader = compileShader(GL_VERTEX_SHADER, vtxShaderSrc);
	unsigned int prog = glCreateProgram();
	glAttachShader(prog, vShader);
	glAttachShader(prog, fShader);
	glLinkProgram(prog);
	int success;
	char log[512];
	glGetProgramiv(prog, GL_LINK_STATUS, &success);
	if(!success)
	{
		glGetProgramInfoLog(prog, 512, NULL, log);
		std::cout << "link failed:" << log << std::endl;
	}
	glDeleteShader(vShader);
	glDeleteShader(fShader);
	return prog;
}

unsigned int createShaderProgramFiles(const char* vtxFile, const char* fragFile)
{
	char* fragSrc, *vtxSrc;
	read_file(vtxFile, &vtxSrc);
	read_file(fragFile, &fragSrc);
	//std::cout << "Compiling Program: Vert: \n" << vtxSrc << "\n Frag: \n" << fragSrc << std::endl; 
	unsigned int prog = createShaderProgram(vtxSrc, fragSrc);
	delete[] fragSrc;
	delete[] vtxSrc;
	return prog;
}

}
