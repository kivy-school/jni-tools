from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer

class GLES20:
    GL_ACTIVE_ATTRIBUTES: ClassVar[int]
    GL_ACTIVE_ATTRIBUTE_MAX_LENGTH: ClassVar[int]
    GL_ACTIVE_TEXTURE: ClassVar[int]
    GL_ACTIVE_UNIFORMS: ClassVar[int]
    GL_ACTIVE_UNIFORM_MAX_LENGTH: ClassVar[int]
    GL_ALIASED_LINE_WIDTH_RANGE: ClassVar[int]
    GL_ALIASED_POINT_SIZE_RANGE: ClassVar[int]
    GL_ALPHA: ClassVar[int]
    GL_ALPHA_BITS: ClassVar[int]
    GL_ALWAYS: ClassVar[int]
    GL_ARRAY_BUFFER: ClassVar[int]
    GL_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_ATTACHED_SHADERS: ClassVar[int]
    GL_BACK: ClassVar[int]
    GL_BLEND: ClassVar[int]
    GL_BLEND_COLOR: ClassVar[int]
    GL_BLEND_DST_ALPHA: ClassVar[int]
    GL_BLEND_DST_RGB: ClassVar[int]
    GL_BLEND_EQUATION: ClassVar[int]
    GL_BLEND_EQUATION_ALPHA: ClassVar[int]
    GL_BLEND_EQUATION_RGB: ClassVar[int]
    GL_BLEND_SRC_ALPHA: ClassVar[int]
    GL_BLEND_SRC_RGB: ClassVar[int]
    GL_BLUE_BITS: ClassVar[int]
    GL_BOOL: ClassVar[int]
    GL_BOOL_VEC2: ClassVar[int]
    GL_BOOL_VEC3: ClassVar[int]
    GL_BOOL_VEC4: ClassVar[int]
    GL_BUFFER_SIZE: ClassVar[int]
    GL_BUFFER_USAGE: ClassVar[int]
    GL_BYTE: ClassVar[int]
    GL_CCW: ClassVar[int]
    GL_CLAMP_TO_EDGE: ClassVar[int]
    GL_COLOR_ATTACHMENT0: ClassVar[int]
    GL_COLOR_BUFFER_BIT: ClassVar[int]
    GL_COLOR_CLEAR_VALUE: ClassVar[int]
    GL_COLOR_WRITEMASK: ClassVar[int]
    GL_COMPILE_STATUS: ClassVar[int]
    GL_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_CONSTANT_ALPHA: ClassVar[int]
    GL_CONSTANT_COLOR: ClassVar[int]
    GL_CULL_FACE: ClassVar[int]
    GL_CULL_FACE_MODE: ClassVar[int]
    GL_CURRENT_PROGRAM: ClassVar[int]
    GL_CURRENT_VERTEX_ATTRIB: ClassVar[int]
    GL_CW: ClassVar[int]
    GL_DECR: ClassVar[int]
    GL_DECR_WRAP: ClassVar[int]
    GL_DELETE_STATUS: ClassVar[int]
    GL_DEPTH_ATTACHMENT: ClassVar[int]
    GL_DEPTH_BITS: ClassVar[int]
    GL_DEPTH_BUFFER_BIT: ClassVar[int]
    GL_DEPTH_CLEAR_VALUE: ClassVar[int]
    GL_DEPTH_COMPONENT: ClassVar[int]
    GL_DEPTH_COMPONENT16: ClassVar[int]
    GL_DEPTH_FUNC: ClassVar[int]
    GL_DEPTH_RANGE: ClassVar[int]
    GL_DEPTH_TEST: ClassVar[int]
    GL_DEPTH_WRITEMASK: ClassVar[int]
    GL_DITHER: ClassVar[int]
    GL_DONT_CARE: ClassVar[int]
    GL_DST_ALPHA: ClassVar[int]
    GL_DST_COLOR: ClassVar[int]
    GL_DYNAMIC_DRAW: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_EQUAL: ClassVar[int]
    GL_EXTENSIONS: ClassVar[int]
    GL_FALSE: ClassVar[int]
    GL_FASTEST: ClassVar[int]
    GL_FIXED: ClassVar[int]
    GL_FLOAT: ClassVar[int]
    GL_FLOAT_MAT2: ClassVar[int]
    GL_FLOAT_MAT3: ClassVar[int]
    GL_FLOAT_MAT4: ClassVar[int]
    GL_FLOAT_VEC2: ClassVar[int]
    GL_FLOAT_VEC3: ClassVar[int]
    GL_FLOAT_VEC4: ClassVar[int]
    GL_FRAGMENT_SHADER: ClassVar[int]
    GL_FRAMEBUFFER: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL: ClassVar[int]
    GL_FRAMEBUFFER_BINDING: ClassVar[int]
    GL_FRAMEBUFFER_COMPLETE: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT: ClassVar[int]
    GL_FRAMEBUFFER_UNSUPPORTED: ClassVar[int]
    GL_FRONT: ClassVar[int]
    GL_FRONT_AND_BACK: ClassVar[int]
    GL_FRONT_FACE: ClassVar[int]
    GL_FUNC_ADD: ClassVar[int]
    GL_FUNC_REVERSE_SUBTRACT: ClassVar[int]
    GL_FUNC_SUBTRACT: ClassVar[int]
    GL_GENERATE_MIPMAP_HINT: ClassVar[int]
    GL_GEQUAL: ClassVar[int]
    GL_GREATER: ClassVar[int]
    GL_GREEN_BITS: ClassVar[int]
    GL_HIGH_FLOAT: ClassVar[int]
    GL_HIGH_INT: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_FORMAT: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_TYPE: ClassVar[int]
    GL_INCR: ClassVar[int]
    GL_INCR_WRAP: ClassVar[int]
    GL_INFO_LOG_LENGTH: ClassVar[int]
    GL_INT: ClassVar[int]
    GL_INT_VEC2: ClassVar[int]
    GL_INT_VEC3: ClassVar[int]
    GL_INT_VEC4: ClassVar[int]
    GL_INVALID_ENUM: ClassVar[int]
    GL_INVALID_FRAMEBUFFER_OPERATION: ClassVar[int]
    GL_INVALID_OPERATION: ClassVar[int]
    GL_INVALID_VALUE: ClassVar[int]
    GL_INVERT: ClassVar[int]
    GL_KEEP: ClassVar[int]
    GL_LEQUAL: ClassVar[int]
    GL_LESS: ClassVar[int]
    GL_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_NEAREST: ClassVar[int]
    GL_LINES: ClassVar[int]
    GL_LINE_LOOP: ClassVar[int]
    GL_LINE_STRIP: ClassVar[int]
    GL_LINE_WIDTH: ClassVar[int]
    GL_LINK_STATUS: ClassVar[int]
    GL_LOW_FLOAT: ClassVar[int]
    GL_LOW_INT: ClassVar[int]
    GL_LUMINANCE: ClassVar[int]
    GL_LUMINANCE_ALPHA: ClassVar[int]
    GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_CUBE_MAP_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_FRAGMENT_UNIFORM_VECTORS: ClassVar[int]
    GL_MAX_RENDERBUFFER_SIZE: ClassVar[int]
    GL_MAX_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_VARYING_VECTORS: ClassVar[int]
    GL_MAX_VERTEX_ATTRIBS: ClassVar[int]
    GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_VERTEX_UNIFORM_VECTORS: ClassVar[int]
    GL_MAX_VIEWPORT_DIMS: ClassVar[int]
    GL_MEDIUM_FLOAT: ClassVar[int]
    GL_MEDIUM_INT: ClassVar[int]
    GL_MIRRORED_REPEAT: ClassVar[int]
    GL_NEAREST: ClassVar[int]
    GL_NEAREST_MIPMAP_LINEAR: ClassVar[int]
    GL_NEAREST_MIPMAP_NEAREST: ClassVar[int]
    GL_NEVER: ClassVar[int]
    GL_NICEST: ClassVar[int]
    GL_NONE: ClassVar[int]
    GL_NOTEQUAL: ClassVar[int]
    GL_NO_ERROR: ClassVar[int]
    GL_NUM_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_NUM_SHADER_BINARY_FORMATS: ClassVar[int]
    GL_ONE: ClassVar[int]
    GL_ONE_MINUS_CONSTANT_ALPHA: ClassVar[int]
    GL_ONE_MINUS_CONSTANT_COLOR: ClassVar[int]
    GL_ONE_MINUS_DST_ALPHA: ClassVar[int]
    GL_ONE_MINUS_DST_COLOR: ClassVar[int]
    GL_ONE_MINUS_SRC_ALPHA: ClassVar[int]
    GL_ONE_MINUS_SRC_COLOR: ClassVar[int]
    GL_OUT_OF_MEMORY: ClassVar[int]
    GL_PACK_ALIGNMENT: ClassVar[int]
    GL_POINTS: ClassVar[int]
    GL_POLYGON_OFFSET_FACTOR: ClassVar[int]
    GL_POLYGON_OFFSET_FILL: ClassVar[int]
    GL_POLYGON_OFFSET_UNITS: ClassVar[int]
    GL_RED_BITS: ClassVar[int]
    GL_RENDERBUFFER: ClassVar[int]
    GL_RENDERBUFFER_ALPHA_SIZE: ClassVar[int]
    GL_RENDERBUFFER_BINDING: ClassVar[int]
    GL_RENDERBUFFER_BLUE_SIZE: ClassVar[int]
    GL_RENDERBUFFER_DEPTH_SIZE: ClassVar[int]
    GL_RENDERBUFFER_GREEN_SIZE: ClassVar[int]
    GL_RENDERBUFFER_HEIGHT: ClassVar[int]
    GL_RENDERBUFFER_INTERNAL_FORMAT: ClassVar[int]
    GL_RENDERBUFFER_RED_SIZE: ClassVar[int]
    GL_RENDERBUFFER_STENCIL_SIZE: ClassVar[int]
    GL_RENDERBUFFER_WIDTH: ClassVar[int]
    GL_RENDERER: ClassVar[int]
    GL_REPEAT: ClassVar[int]
    GL_REPLACE: ClassVar[int]
    GL_RGB: ClassVar[int]
    GL_RGB565: ClassVar[int]
    GL_RGB5_A1: ClassVar[int]
    GL_RGBA: ClassVar[int]
    GL_RGBA4: ClassVar[int]
    GL_SAMPLER_2D: ClassVar[int]
    GL_SAMPLER_CUBE: ClassVar[int]
    GL_SAMPLES: ClassVar[int]
    GL_SAMPLE_ALPHA_TO_COVERAGE: ClassVar[int]
    GL_SAMPLE_BUFFERS: ClassVar[int]
    GL_SAMPLE_COVERAGE: ClassVar[int]
    GL_SAMPLE_COVERAGE_INVERT: ClassVar[int]
    GL_SAMPLE_COVERAGE_VALUE: ClassVar[int]
    GL_SCISSOR_BOX: ClassVar[int]
    GL_SCISSOR_TEST: ClassVar[int]
    GL_SHADER_BINARY_FORMATS: ClassVar[int]
    GL_SHADER_COMPILER: ClassVar[int]
    GL_SHADER_SOURCE_LENGTH: ClassVar[int]
    GL_SHADER_TYPE: ClassVar[int]
    GL_SHADING_LANGUAGE_VERSION: ClassVar[int]
    GL_SHORT: ClassVar[int]
    GL_SRC_ALPHA: ClassVar[int]
    GL_SRC_ALPHA_SATURATE: ClassVar[int]
    GL_SRC_COLOR: ClassVar[int]
    GL_STATIC_DRAW: ClassVar[int]
    GL_STENCIL_ATTACHMENT: ClassVar[int]
    GL_STENCIL_BACK_FAIL: ClassVar[int]
    GL_STENCIL_BACK_FUNC: ClassVar[int]
    GL_STENCIL_BACK_PASS_DEPTH_FAIL: ClassVar[int]
    GL_STENCIL_BACK_PASS_DEPTH_PASS: ClassVar[int]
    GL_STENCIL_BACK_REF: ClassVar[int]
    GL_STENCIL_BACK_VALUE_MASK: ClassVar[int]
    GL_STENCIL_BACK_WRITEMASK: ClassVar[int]
    GL_STENCIL_BITS: ClassVar[int]
    GL_STENCIL_BUFFER_BIT: ClassVar[int]
    GL_STENCIL_CLEAR_VALUE: ClassVar[int]
    GL_STENCIL_FAIL: ClassVar[int]
    GL_STENCIL_FUNC: ClassVar[int]
    GL_STENCIL_INDEX: ClassVar[int]
    GL_STENCIL_INDEX8: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_FAIL: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_PASS: ClassVar[int]
    GL_STENCIL_REF: ClassVar[int]
    GL_STENCIL_TEST: ClassVar[int]
    GL_STENCIL_VALUE_MASK: ClassVar[int]
    GL_STENCIL_WRITEMASK: ClassVar[int]
    GL_STREAM_DRAW: ClassVar[int]
    GL_SUBPIXEL_BITS: ClassVar[int]
    GL_TEXTURE: ClassVar[int]
    GL_TEXTURE0: ClassVar[int]
    GL_TEXTURE1: ClassVar[int]
    GL_TEXTURE10: ClassVar[int]
    GL_TEXTURE11: ClassVar[int]
    GL_TEXTURE12: ClassVar[int]
    GL_TEXTURE13: ClassVar[int]
    GL_TEXTURE14: ClassVar[int]
    GL_TEXTURE15: ClassVar[int]
    GL_TEXTURE16: ClassVar[int]
    GL_TEXTURE17: ClassVar[int]
    GL_TEXTURE18: ClassVar[int]
    GL_TEXTURE19: ClassVar[int]
    GL_TEXTURE2: ClassVar[int]
    GL_TEXTURE20: ClassVar[int]
    GL_TEXTURE21: ClassVar[int]
    GL_TEXTURE22: ClassVar[int]
    GL_TEXTURE23: ClassVar[int]
    GL_TEXTURE24: ClassVar[int]
    GL_TEXTURE25: ClassVar[int]
    GL_TEXTURE26: ClassVar[int]
    GL_TEXTURE27: ClassVar[int]
    GL_TEXTURE28: ClassVar[int]
    GL_TEXTURE29: ClassVar[int]
    GL_TEXTURE3: ClassVar[int]
    GL_TEXTURE30: ClassVar[int]
    GL_TEXTURE31: ClassVar[int]
    GL_TEXTURE4: ClassVar[int]
    GL_TEXTURE5: ClassVar[int]
    GL_TEXTURE6: ClassVar[int]
    GL_TEXTURE7: ClassVar[int]
    GL_TEXTURE8: ClassVar[int]
    GL_TEXTURE9: ClassVar[int]
    GL_TEXTURE_2D: ClassVar[int]
    GL_TEXTURE_BINDING_2D: ClassVar[int]
    GL_TEXTURE_BINDING_CUBE_MAP: ClassVar[int]
    GL_TEXTURE_CUBE_MAP: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_X: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_X: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Y: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Z: ClassVar[int]
    GL_TEXTURE_MAG_FILTER: ClassVar[int]
    GL_TEXTURE_MIN_FILTER: ClassVar[int]
    GL_TEXTURE_WRAP_S: ClassVar[int]
    GL_TEXTURE_WRAP_T: ClassVar[int]
    GL_TRIANGLES: ClassVar[int]
    GL_TRIANGLE_FAN: ClassVar[int]
    GL_TRIANGLE_STRIP: ClassVar[int]
    GL_TRUE: ClassVar[int]
    GL_UNPACK_ALIGNMENT: ClassVar[int]
    GL_UNSIGNED_BYTE: ClassVar[int]
    GL_UNSIGNED_INT: ClassVar[int]
    GL_UNSIGNED_SHORT: ClassVar[int]
    GL_UNSIGNED_SHORT_4_4_4_4: ClassVar[int]
    GL_UNSIGNED_SHORT_5_5_5_1: ClassVar[int]
    GL_UNSIGNED_SHORT_5_6_5: ClassVar[int]
    GL_VALIDATE_STATUS: ClassVar[int]
    GL_VENDOR: ClassVar[int]
    GL_VERSION: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_ENABLED: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_NORMALIZED: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_POINTER: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_SIZE: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_STRIDE: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_TYPE: ClassVar[int]
    GL_VERTEX_SHADER: ClassVar[int]
    GL_VIEWPORT: ClassVar[int]
    GL_ZERO: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def glActiveTexture(p0: int) -> None: ...
    @staticmethod
    def glAttachShader(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindAttribLocation(p0: int, p1: int, p2: str) -> None: ...
    @staticmethod
    def glBindBuffer(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindFramebuffer(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindRenderbuffer(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendColor(p0: float, p1: float, p2: float, p3: float) -> None: ...
    @staticmethod
    def glBlendEquation(p0: int) -> None: ...
    @staticmethod
    def glBlendEquationSeparate(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendFuncSeparate(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glBufferData(p0: int, p1: int, p2: Buffer, p3: int) -> None: ...
    @staticmethod
    def glBufferSubData(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @staticmethod
    def glCheckFramebufferStatus(p0: int) -> int: ...
    @staticmethod
    def glCompileShader(p0: int) -> None: ...
    @staticmethod
    def glCreateProgram() -> int: ...
    @staticmethod
    def glCreateShader(p0: int) -> int: ...
    @overload
    @staticmethod
    def glDeleteBuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteBuffers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteFramebuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteFramebuffers(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glDeleteProgram(p0: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteRenderbuffers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteRenderbuffers(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glDeleteShader(p0: int) -> None: ...
    @staticmethod
    def glDetachShader(p0: int, p1: int) -> None: ...
    @staticmethod
    def glDisableVertexAttribArray(p0: int) -> None: ...
    @staticmethod
    def glEnableVertexAttribArray(p0: int) -> None: ...
    @staticmethod
    def glFramebufferRenderbuffer(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glFramebufferTexture2D(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGenBuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenBuffers(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glGenerateMipmap(p0: int) -> None: ...
    @overload
    @staticmethod
    def glGenFramebuffers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGenFramebuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenRenderbuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenRenderbuffers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveAttrib(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> str: ...
    @overload
    @staticmethod
    def glGetActiveAttrib(p0: int, p1: int, p2: IntBuffer, p3: IntBuffer) -> str: ...
    @overload
    @staticmethod
    def glGetActiveAttrib(p0: int, p1: int, p2: int, p3: Any, p4: int, p5: Any, p6: int, p7: Any, p8: int, p9: Any, p10: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniform(p0: int, p1: int, p2: int, p3: Any, p4: int, p5: Any, p6: int, p7: Any, p8: int, p9: Any, p10: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniform(p0: int, p1: int, p2: IntBuffer, p3: IntBuffer) -> str: ...
    @overload
    @staticmethod
    def glGetActiveUniform(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> str: ...
    @overload
    @staticmethod
    def glGetAttachedShaders(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glGetAttachedShaders(p0: int, p1: int, p2: IntBuffer, p3: IntBuffer) -> None: ...
    @staticmethod
    def glGetAttribLocation(p0: int, p1: str) -> int: ...
    @overload
    @staticmethod
    def glGetBooleanv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetBooleanv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetFloatv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetFloatv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferAttachmentParameteriv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferAttachmentParameteriv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGetProgramiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetProgramiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glGetProgramInfoLog(p0: int) -> str: ...
    @overload
    @staticmethod
    def glGetRenderbufferParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetRenderbufferParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetShaderiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetShaderiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glGetShaderInfoLog(p0: int) -> str: ...
    @overload
    @staticmethod
    def glGetShaderPrecisionFormat(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glGetShaderPrecisionFormat(p0: int, p1: int, p2: IntBuffer, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetShaderSource(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glGetShaderSource(p0: int) -> str: ...
    @overload
    @staticmethod
    def glGetTexParameterfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetUniformfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetUniformfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetUniformiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetUniformiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glGetUniformLocation(p0: int, p1: str) -> int: ...
    @overload
    @staticmethod
    def glGetVertexAttribfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glIsBuffer(p0: int) -> bool: ...
    @staticmethod
    def glIsEnabled(p0: int) -> bool: ...
    @staticmethod
    def glIsFramebuffer(p0: int) -> bool: ...
    @staticmethod
    def glIsProgram(p0: int) -> bool: ...
    @staticmethod
    def glIsRenderbuffer(p0: int) -> bool: ...
    @staticmethod
    def glIsShader(p0: int) -> bool: ...
    @staticmethod
    def glIsTexture(p0: int) -> bool: ...
    @staticmethod
    def glLinkProgram(p0: int) -> None: ...
    @staticmethod
    def glReleaseShaderCompiler() -> None: ...
    @staticmethod
    def glRenderbufferStorage(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glShaderBinary(p0: int, p1: IntBuffer, p2: int, p3: Buffer, p4: int) -> None: ...
    @overload
    @staticmethod
    def glShaderBinary(p0: int, p1: Any, p2: int, p3: int, p4: Buffer, p5: int) -> None: ...
    @staticmethod
    def glShaderSource(p0: int, p1: str) -> None: ...
    @staticmethod
    def glStencilFuncSeparate(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glStencilMaskSeparate(p0: int, p1: int) -> None: ...
    @staticmethod
    def glStencilOpSeparate(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glTexParameteri(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glUniform1f(p0: int, p1: float) -> None: ...
    @overload
    @staticmethod
    def glUniform1fv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform1fv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glUniform1i(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glUniform1iv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform1iv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glUniform2f(p0: int, p1: float, p2: float) -> None: ...
    @overload
    @staticmethod
    def glUniform2fv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform2fv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glUniform2i(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glUniform2iv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform2iv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glUniform3f(p0: int, p1: float, p2: float, p3: float) -> None: ...
    @overload
    @staticmethod
    def glUniform3fv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform3fv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glUniform3i(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform3iv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform3iv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glUniform4f(p0: int, p1: float, p2: float, p3: float, p4: float) -> None: ...
    @overload
    @staticmethod
    def glUniform4fv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform4fv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glUniform4i(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniform4iv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform4iv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @staticmethod
    def glUseProgram(p0: int) -> None: ...
    @staticmethod
    def glValidateProgram(p0: int) -> None: ...
    @staticmethod
    def glVertexAttrib1f(p0: int, p1: float) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib1fv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib1fv(p0: int, p1: FloatBuffer) -> None: ...
    @staticmethod
    def glVertexAttrib2f(p0: int, p1: float, p2: float) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib2fv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib2fv(p0: int, p1: FloatBuffer) -> None: ...
    @staticmethod
    def glVertexAttrib3f(p0: int, p1: float, p2: float, p3: float) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib3fv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib3fv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glVertexAttrib4f(p0: int, p1: float, p2: float, p3: float, p4: float) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib4fv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib4fv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribPointer(p0: int, p1: int, p2: int, p3: bool, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribPointer(p0: int, p1: int, p2: int, p3: bool, p4: int, p5: Buffer) -> None: ...
    @staticmethod
    def glHint(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindTexture(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendFunc(p0: int, p1: int) -> None: ...
    @staticmethod
    def glClear(p0: int) -> None: ...
    @staticmethod
    def glClearColor(p0: float, p1: float, p2: float, p3: float) -> None: ...
    @staticmethod
    def glClearDepthf(p0: float) -> None: ...
    @staticmethod
    def glClearStencil(p0: int) -> None: ...
    @staticmethod
    def glColorMask(p0: bool, p1: bool, p2: bool, p3: bool) -> None: ...
    @staticmethod
    def glCompressedTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: Buffer) -> None: ...
    @staticmethod
    def glCompressedTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @staticmethod
    def glCopyTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @staticmethod
    def glCopyTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @staticmethod
    def glCullFace(p0: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteTextures(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteTextures(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glDepthFunc(p0: int) -> None: ...
    @staticmethod
    def glDepthMask(p0: bool) -> None: ...
    @staticmethod
    def glDepthRangef(p0: float, p1: float) -> None: ...
    @staticmethod
    def glDisable(p0: int) -> None: ...
    @staticmethod
    def glDrawArrays(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDrawElements(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glDrawElements(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @staticmethod
    def glEnable(p0: int) -> None: ...
    @staticmethod
    def glFinish() -> None: ...
    @staticmethod
    def glFlush() -> None: ...
    @staticmethod
    def glFrontFace(p0: int) -> None: ...
    @overload
    @staticmethod
    def glGenTextures(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenTextures(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glGetError() -> int: ...
    @overload
    @staticmethod
    def glGetIntegerv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetIntegerv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glGetString(p0: int) -> str: ...
    @staticmethod
    def glLineWidth(p0: float) -> None: ...
    @staticmethod
    def glPixelStorei(p0: int, p1: int) -> None: ...
    @staticmethod
    def glPolygonOffset(p0: float, p1: float) -> None: ...
    @staticmethod
    def glReadPixels(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: Buffer) -> None: ...
    @staticmethod
    def glSampleCoverage(p0: float, p1: bool) -> None: ...
    @staticmethod
    def glScissor(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glStencilFunc(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glStencilMask(p0: int) -> None: ...
    @staticmethod
    def glStencilOp(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @staticmethod
    def glTexParameterf(p0: int, p1: int, p2: float) -> None: ...
    @staticmethod
    def glTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @staticmethod
    def glViewport(p0: int, p1: int, p2: int, p3: int) -> None: ...
