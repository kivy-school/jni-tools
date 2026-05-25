from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.ByteBuffer import ByteBuffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer
from java.nio.LongBuffer import LongBuffer

class GLES30:
    GL_ACTIVE_UNIFORM_BLOCKS: ClassVar[int]
    GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH: ClassVar[int]
    GL_ALREADY_SIGNALED: ClassVar[int]
    GL_ANY_SAMPLES_PASSED: ClassVar[int]
    GL_ANY_SAMPLES_PASSED_CONSERVATIVE: ClassVar[int]
    GL_BLUE: ClassVar[int]
    GL_BUFFER_ACCESS_FLAGS: ClassVar[int]
    GL_BUFFER_MAPPED: ClassVar[int]
    GL_BUFFER_MAP_LENGTH: ClassVar[int]
    GL_BUFFER_MAP_OFFSET: ClassVar[int]
    GL_BUFFER_MAP_POINTER: ClassVar[int]
    GL_COLOR: ClassVar[int]
    GL_COLOR_ATTACHMENT1: ClassVar[int]
    GL_COLOR_ATTACHMENT10: ClassVar[int]
    GL_COLOR_ATTACHMENT11: ClassVar[int]
    GL_COLOR_ATTACHMENT12: ClassVar[int]
    GL_COLOR_ATTACHMENT13: ClassVar[int]
    GL_COLOR_ATTACHMENT14: ClassVar[int]
    GL_COLOR_ATTACHMENT15: ClassVar[int]
    GL_COLOR_ATTACHMENT2: ClassVar[int]
    GL_COLOR_ATTACHMENT3: ClassVar[int]
    GL_COLOR_ATTACHMENT4: ClassVar[int]
    GL_COLOR_ATTACHMENT5: ClassVar[int]
    GL_COLOR_ATTACHMENT6: ClassVar[int]
    GL_COLOR_ATTACHMENT7: ClassVar[int]
    GL_COLOR_ATTACHMENT8: ClassVar[int]
    GL_COLOR_ATTACHMENT9: ClassVar[int]
    GL_COMPARE_REF_TO_TEXTURE: ClassVar[int]
    GL_COMPRESSED_R11_EAC: ClassVar[int]
    GL_COMPRESSED_RG11_EAC: ClassVar[int]
    GL_COMPRESSED_RGB8_ETC2: ClassVar[int]
    GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2: ClassVar[int]
    GL_COMPRESSED_RGBA8_ETC2_EAC: ClassVar[int]
    GL_COMPRESSED_SIGNED_R11_EAC: ClassVar[int]
    GL_COMPRESSED_SIGNED_RG11_EAC: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC: ClassVar[int]
    GL_COMPRESSED_SRGB8_ETC2: ClassVar[int]
    GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2: ClassVar[int]
    GL_CONDITION_SATISFIED: ClassVar[int]
    GL_COPY_READ_BUFFER: ClassVar[int]
    GL_COPY_READ_BUFFER_BINDING: ClassVar[int]
    GL_COPY_WRITE_BUFFER: ClassVar[int]
    GL_COPY_WRITE_BUFFER_BINDING: ClassVar[int]
    GL_CURRENT_QUERY: ClassVar[int]
    GL_DEPTH: ClassVar[int]
    GL_DEPTH24_STENCIL8: ClassVar[int]
    GL_DEPTH32F_STENCIL8: ClassVar[int]
    GL_DEPTH_COMPONENT24: ClassVar[int]
    GL_DEPTH_COMPONENT32F: ClassVar[int]
    GL_DEPTH_STENCIL: ClassVar[int]
    GL_DEPTH_STENCIL_ATTACHMENT: ClassVar[int]
    GL_DRAW_BUFFER0: ClassVar[int]
    GL_DRAW_BUFFER1: ClassVar[int]
    GL_DRAW_BUFFER10: ClassVar[int]
    GL_DRAW_BUFFER11: ClassVar[int]
    GL_DRAW_BUFFER12: ClassVar[int]
    GL_DRAW_BUFFER13: ClassVar[int]
    GL_DRAW_BUFFER14: ClassVar[int]
    GL_DRAW_BUFFER15: ClassVar[int]
    GL_DRAW_BUFFER2: ClassVar[int]
    GL_DRAW_BUFFER3: ClassVar[int]
    GL_DRAW_BUFFER4: ClassVar[int]
    GL_DRAW_BUFFER5: ClassVar[int]
    GL_DRAW_BUFFER6: ClassVar[int]
    GL_DRAW_BUFFER7: ClassVar[int]
    GL_DRAW_BUFFER8: ClassVar[int]
    GL_DRAW_BUFFER9: ClassVar[int]
    GL_DRAW_FRAMEBUFFER: ClassVar[int]
    GL_DRAW_FRAMEBUFFER_BINDING: ClassVar[int]
    GL_DYNAMIC_COPY: ClassVar[int]
    GL_DYNAMIC_READ: ClassVar[int]
    GL_FLOAT_32_UNSIGNED_INT_24_8_REV: ClassVar[int]
    GL_FLOAT_MAT2x3: ClassVar[int]
    GL_FLOAT_MAT2x4: ClassVar[int]
    GL_FLOAT_MAT3x2: ClassVar[int]
    GL_FLOAT_MAT3x4: ClassVar[int]
    GL_FLOAT_MAT4x2: ClassVar[int]
    GL_FLOAT_MAT4x3: ClassVar[int]
    GL_FRAGMENT_SHADER_DERIVATIVE_HINT: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE: ClassVar[int]
    GL_FRAMEBUFFER_UNDEFINED: ClassVar[int]
    GL_GREEN: ClassVar[int]
    GL_HALF_FLOAT: ClassVar[int]
    GL_INTERLEAVED_ATTRIBS: ClassVar[int]
    GL_INT_2_10_10_10_REV: ClassVar[int]
    GL_INT_SAMPLER_2D: ClassVar[int]
    GL_INT_SAMPLER_2D_ARRAY: ClassVar[int]
    GL_INT_SAMPLER_3D: ClassVar[int]
    GL_INT_SAMPLER_CUBE: ClassVar[int]
    GL_INVALID_INDEX: ClassVar[int]
    GL_MAJOR_VERSION: ClassVar[int]
    GL_MAP_FLUSH_EXPLICIT_BIT: ClassVar[int]
    GL_MAP_INVALIDATE_BUFFER_BIT: ClassVar[int]
    GL_MAP_INVALIDATE_RANGE_BIT: ClassVar[int]
    GL_MAP_READ_BIT: ClassVar[int]
    GL_MAP_UNSYNCHRONIZED_BIT: ClassVar[int]
    GL_MAP_WRITE_BIT: ClassVar[int]
    GL_MAX: ClassVar[int]
    GL_MAX_3D_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_ARRAY_TEXTURE_LAYERS: ClassVar[int]
    GL_MAX_COLOR_ATTACHMENTS: ClassVar[int]
    GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMBINED_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_DRAW_BUFFERS: ClassVar[int]
    GL_MAX_ELEMENTS_INDICES: ClassVar[int]
    GL_MAX_ELEMENTS_VERTICES: ClassVar[int]
    GL_MAX_ELEMENT_INDEX: ClassVar[int]
    GL_MAX_FRAGMENT_INPUT_COMPONENTS: ClassVar[int]
    GL_MAX_FRAGMENT_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_FRAGMENT_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_PROGRAM_TEXEL_OFFSET: ClassVar[int]
    GL_MAX_SAMPLES: ClassVar[int]
    GL_MAX_SERVER_WAIT_TIMEOUT: ClassVar[int]
    GL_MAX_TEXTURE_LOD_BIAS: ClassVar[int]
    GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS: ClassVar[int]
    GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS: ClassVar[int]
    GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS: ClassVar[int]
    GL_MAX_UNIFORM_BLOCK_SIZE: ClassVar[int]
    GL_MAX_UNIFORM_BUFFER_BINDINGS: ClassVar[int]
    GL_MAX_VARYING_COMPONENTS: ClassVar[int]
    GL_MAX_VERTEX_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_VERTEX_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_VERTEX_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MIN: ClassVar[int]
    GL_MINOR_VERSION: ClassVar[int]
    GL_MIN_PROGRAM_TEXEL_OFFSET: ClassVar[int]
    GL_NUM_EXTENSIONS: ClassVar[int]
    GL_NUM_PROGRAM_BINARY_FORMATS: ClassVar[int]
    GL_NUM_SAMPLE_COUNTS: ClassVar[int]
    GL_OBJECT_TYPE: ClassVar[int]
    GL_PACK_ROW_LENGTH: ClassVar[int]
    GL_PACK_SKIP_PIXELS: ClassVar[int]
    GL_PACK_SKIP_ROWS: ClassVar[int]
    GL_PIXEL_PACK_BUFFER: ClassVar[int]
    GL_PIXEL_PACK_BUFFER_BINDING: ClassVar[int]
    GL_PIXEL_UNPACK_BUFFER: ClassVar[int]
    GL_PIXEL_UNPACK_BUFFER_BINDING: ClassVar[int]
    GL_PRIMITIVE_RESTART_FIXED_INDEX: ClassVar[int]
    GL_PROGRAM_BINARY_FORMATS: ClassVar[int]
    GL_PROGRAM_BINARY_LENGTH: ClassVar[int]
    GL_PROGRAM_BINARY_RETRIEVABLE_HINT: ClassVar[int]
    GL_QUERY_RESULT: ClassVar[int]
    GL_QUERY_RESULT_AVAILABLE: ClassVar[int]
    GL_R11F_G11F_B10F: ClassVar[int]
    GL_R16F: ClassVar[int]
    GL_R16I: ClassVar[int]
    GL_R16UI: ClassVar[int]
    GL_R32F: ClassVar[int]
    GL_R32I: ClassVar[int]
    GL_R32UI: ClassVar[int]
    GL_R8: ClassVar[int]
    GL_R8I: ClassVar[int]
    GL_R8UI: ClassVar[int]
    GL_R8_SNORM: ClassVar[int]
    GL_RASTERIZER_DISCARD: ClassVar[int]
    GL_READ_BUFFER: ClassVar[int]
    GL_READ_FRAMEBUFFER: ClassVar[int]
    GL_READ_FRAMEBUFFER_BINDING: ClassVar[int]
    GL_RED: ClassVar[int]
    GL_RED_INTEGER: ClassVar[int]
    GL_RENDERBUFFER_SAMPLES: ClassVar[int]
    GL_RG: ClassVar[int]
    GL_RG16F: ClassVar[int]
    GL_RG16I: ClassVar[int]
    GL_RG16UI: ClassVar[int]
    GL_RG32F: ClassVar[int]
    GL_RG32I: ClassVar[int]
    GL_RG32UI: ClassVar[int]
    GL_RG8: ClassVar[int]
    GL_RG8I: ClassVar[int]
    GL_RG8UI: ClassVar[int]
    GL_RG8_SNORM: ClassVar[int]
    GL_RGB10_A2: ClassVar[int]
    GL_RGB10_A2UI: ClassVar[int]
    GL_RGB16F: ClassVar[int]
    GL_RGB16I: ClassVar[int]
    GL_RGB16UI: ClassVar[int]
    GL_RGB32F: ClassVar[int]
    GL_RGB32I: ClassVar[int]
    GL_RGB32UI: ClassVar[int]
    GL_RGB8: ClassVar[int]
    GL_RGB8I: ClassVar[int]
    GL_RGB8UI: ClassVar[int]
    GL_RGB8_SNORM: ClassVar[int]
    GL_RGB9_E5: ClassVar[int]
    GL_RGBA16F: ClassVar[int]
    GL_RGBA16I: ClassVar[int]
    GL_RGBA16UI: ClassVar[int]
    GL_RGBA32F: ClassVar[int]
    GL_RGBA32I: ClassVar[int]
    GL_RGBA32UI: ClassVar[int]
    GL_RGBA8: ClassVar[int]
    GL_RGBA8I: ClassVar[int]
    GL_RGBA8UI: ClassVar[int]
    GL_RGBA8_SNORM: ClassVar[int]
    GL_RGBA_INTEGER: ClassVar[int]
    GL_RGB_INTEGER: ClassVar[int]
    GL_RG_INTEGER: ClassVar[int]
    GL_SAMPLER_2D_ARRAY: ClassVar[int]
    GL_SAMPLER_2D_ARRAY_SHADOW: ClassVar[int]
    GL_SAMPLER_2D_SHADOW: ClassVar[int]
    GL_SAMPLER_3D: ClassVar[int]
    GL_SAMPLER_BINDING: ClassVar[int]
    GL_SAMPLER_CUBE_SHADOW: ClassVar[int]
    GL_SEPARATE_ATTRIBS: ClassVar[int]
    GL_SIGNALED: ClassVar[int]
    GL_SIGNED_NORMALIZED: ClassVar[int]
    GL_SRGB: ClassVar[int]
    GL_SRGB8: ClassVar[int]
    GL_SRGB8_ALPHA8: ClassVar[int]
    GL_STATIC_COPY: ClassVar[int]
    GL_STATIC_READ: ClassVar[int]
    GL_STENCIL: ClassVar[int]
    GL_STREAM_COPY: ClassVar[int]
    GL_STREAM_READ: ClassVar[int]
    GL_SYNC_CONDITION: ClassVar[int]
    GL_SYNC_FENCE: ClassVar[int]
    GL_SYNC_FLAGS: ClassVar[int]
    GL_SYNC_FLUSH_COMMANDS_BIT: ClassVar[int]
    GL_SYNC_GPU_COMMANDS_COMPLETE: ClassVar[int]
    GL_SYNC_STATUS: ClassVar[int]
    GL_TEXTURE_2D_ARRAY: ClassVar[int]
    GL_TEXTURE_3D: ClassVar[int]
    GL_TEXTURE_BASE_LEVEL: ClassVar[int]
    GL_TEXTURE_BINDING_2D_ARRAY: ClassVar[int]
    GL_TEXTURE_BINDING_3D: ClassVar[int]
    GL_TEXTURE_COMPARE_FUNC: ClassVar[int]
    GL_TEXTURE_COMPARE_MODE: ClassVar[int]
    GL_TEXTURE_IMMUTABLE_FORMAT: ClassVar[int]
    GL_TEXTURE_IMMUTABLE_LEVELS: ClassVar[int]
    GL_TEXTURE_MAX_LEVEL: ClassVar[int]
    GL_TEXTURE_MAX_LOD: ClassVar[int]
    GL_TEXTURE_MIN_LOD: ClassVar[int]
    GL_TEXTURE_SWIZZLE_A: ClassVar[int]
    GL_TEXTURE_SWIZZLE_B: ClassVar[int]
    GL_TEXTURE_SWIZZLE_G: ClassVar[int]
    GL_TEXTURE_SWIZZLE_R: ClassVar[int]
    GL_TEXTURE_WRAP_R: ClassVar[int]
    GL_TIMEOUT_EXPIRED: ClassVar[int]
    GL_TIMEOUT_IGNORED: ClassVar[int]
    GL_TRANSFORM_FEEDBACK: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_ACTIVE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BINDING: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_BINDING: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_MODE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_SIZE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_START: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_PAUSED: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_VARYINGS: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH: ClassVar[int]
    GL_UNIFORM_ARRAY_STRIDE: ClassVar[int]
    GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS: ClassVar[int]
    GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES: ClassVar[int]
    GL_UNIFORM_BLOCK_BINDING: ClassVar[int]
    GL_UNIFORM_BLOCK_DATA_SIZE: ClassVar[int]
    GL_UNIFORM_BLOCK_INDEX: ClassVar[int]
    GL_UNIFORM_BLOCK_NAME_LENGTH: ClassVar[int]
    GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER: ClassVar[int]
    GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER: ClassVar[int]
    GL_UNIFORM_BUFFER: ClassVar[int]
    GL_UNIFORM_BUFFER_BINDING: ClassVar[int]
    GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT: ClassVar[int]
    GL_UNIFORM_BUFFER_SIZE: ClassVar[int]
    GL_UNIFORM_BUFFER_START: ClassVar[int]
    GL_UNIFORM_IS_ROW_MAJOR: ClassVar[int]
    GL_UNIFORM_MATRIX_STRIDE: ClassVar[int]
    GL_UNIFORM_NAME_LENGTH: ClassVar[int]
    GL_UNIFORM_OFFSET: ClassVar[int]
    GL_UNIFORM_SIZE: ClassVar[int]
    GL_UNIFORM_TYPE: ClassVar[int]
    GL_UNPACK_IMAGE_HEIGHT: ClassVar[int]
    GL_UNPACK_ROW_LENGTH: ClassVar[int]
    GL_UNPACK_SKIP_IMAGES: ClassVar[int]
    GL_UNPACK_SKIP_PIXELS: ClassVar[int]
    GL_UNPACK_SKIP_ROWS: ClassVar[int]
    GL_UNSIGNALED: ClassVar[int]
    GL_UNSIGNED_INT_10F_11F_11F_REV: ClassVar[int]
    GL_UNSIGNED_INT_24_8: ClassVar[int]
    GL_UNSIGNED_INT_2_10_10_10_REV: ClassVar[int]
    GL_UNSIGNED_INT_5_9_9_9_REV: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D_ARRAY: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_3D: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_CUBE: ClassVar[int]
    GL_UNSIGNED_INT_VEC2: ClassVar[int]
    GL_UNSIGNED_INT_VEC3: ClassVar[int]
    GL_UNSIGNED_INT_VEC4: ClassVar[int]
    GL_UNSIGNED_NORMALIZED: ClassVar[int]
    GL_VERTEX_ARRAY_BINDING: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_DIVISOR: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_INTEGER: ClassVar[int]
    GL_WAIT_FAILED: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def glReadBuffer(arg0: int) -> None: ...
    @overload
    @staticmethod
    def glDrawRangeElements(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: Buffer) -> None: ...
    @overload
    @staticmethod
    def glDrawRangeElements(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...
    @overload
    @staticmethod
    def glTexImage3D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: Buffer) -> None: ...
    @overload
    @staticmethod
    def glTexImage3D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> None: ...
    @overload
    @staticmethod
    def glTexSubImage3D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: Buffer) -> None: ...
    @overload
    @staticmethod
    def glTexSubImage3D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> None: ...
    @staticmethod
    def glCopyTexSubImage3D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> None: ...
    @overload
    @staticmethod
    def glCompressedTexImage3D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: Buffer) -> None: ...
    @overload
    @staticmethod
    def glCompressedTexImage3D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> None: ...
    @overload
    @staticmethod
    def glCompressedTexSubImage3D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: Buffer) -> None: ...
    @overload
    @staticmethod
    def glCompressedTexSubImage3D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> None: ...
    @overload
    @staticmethod
    def glGenQueries(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGenQueries(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteQueries(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteQueries(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glIsQuery(arg0: int) -> bool: ...
    @staticmethod
    def glBeginQuery(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glEndQuery(arg0: int) -> None: ...
    @overload
    @staticmethod
    def glGetQueryiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetQueryiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetQueryObjectuiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetQueryObjectuiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glUnmapBuffer(arg0: int) -> bool: ...
    @staticmethod
    def glGetBufferPointerv(arg0: int, arg1: int) -> Buffer: ...
    @overload
    @staticmethod
    def glDrawBuffers(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glDrawBuffers(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2x3fv(arg0: int, arg1: int, arg2: bool, arg3: list[float], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2x3fv(arg0: int, arg1: int, arg2: bool, arg3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3x2fv(arg0: int, arg1: int, arg2: bool, arg3: list[float], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3x2fv(arg0: int, arg1: int, arg2: bool, arg3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2x4fv(arg0: int, arg1: int, arg2: bool, arg3: list[float], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2x4fv(arg0: int, arg1: int, arg2: bool, arg3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4x2fv(arg0: int, arg1: int, arg2: bool, arg3: list[float], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4x2fv(arg0: int, arg1: int, arg2: bool, arg3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3x4fv(arg0: int, arg1: int, arg2: bool, arg3: list[float], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3x4fv(arg0: int, arg1: int, arg2: bool, arg3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4x3fv(arg0: int, arg1: int, arg2: bool, arg3: list[float], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4x3fv(arg0: int, arg1: int, arg2: bool, arg3: FloatBuffer) -> None: ...
    @staticmethod
    def glBlitFramebuffer(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> None: ...
    @staticmethod
    def glRenderbufferStorageMultisample(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glFramebufferTextureLayer(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glMapBufferRange(arg0: int, arg1: int, arg2: int, arg3: int) -> Buffer: ...
    @staticmethod
    def glFlushMappedBufferRange(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glBindVertexArray(arg0: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteVertexArrays(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteVertexArrays(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenVertexArrays(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGenVertexArrays(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glIsVertexArray(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def glGetIntegeri_v(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetIntegeri_v(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glBeginTransformFeedback(arg0: int) -> None: ...
    @staticmethod
    def glEndTransformFeedback() -> None: ...
    @staticmethod
    def glBindBufferRange(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glBindBufferBase(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glTransformFeedbackVaryings(arg0: int, arg1: list[str], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int, arg5: list[int], arg6: int, arg7: list[int], arg8: int, arg9: list[int], arg10: int) -> None: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(arg0: int, arg1: int, arg2: int, arg3: IntBuffer, arg4: IntBuffer, arg5: IntBuffer, arg6: int) -> None: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(arg0: int, arg1: int, arg2: int, arg3: IntBuffer, arg4: IntBuffer, arg5: IntBuffer, arg6: ByteBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(arg0: int, arg1: int, arg2: list[int], arg3: int, arg4: list[int], arg5: int) -> str: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(arg0: int, arg1: int, arg2: IntBuffer, arg3: IntBuffer) -> str: ...
    @overload
    @staticmethod
    def glVertexAttribIPointer(arg0: int, arg1: int, arg2: int, arg3: int, arg4: Buffer) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribIPointer(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribIiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribIiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribIuiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribIuiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glVertexAttribI4i(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glVertexAttribI4ui(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribI4iv(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribI4iv(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribI4uiv(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribI4uiv(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetUniformuiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetUniformuiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glGetFragDataLocation(arg0: int, arg1: str) -> int: ...
    @staticmethod
    def glUniform1ui(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glUniform2ui(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glUniform3ui(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glUniform4ui(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @overload
    @staticmethod
    def glUniform1uiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform1uiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform2uiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform2uiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform3uiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform3uiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform4uiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform4uiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glClearBufferiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glClearBufferiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glClearBufferuiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glClearBufferuiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glClearBufferfv(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glClearBufferfv(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @staticmethod
    def glClearBufferfi(arg0: int, arg1: int, arg2: float, arg3: int) -> None: ...
    @staticmethod
    def glGetStringi(arg0: int, arg1: int) -> str: ...
    @staticmethod
    def glCopyBufferSubData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @overload
    @staticmethod
    def glGetUniformIndices(arg0: int, arg1: list[str], arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetUniformIndices(arg0: int, arg1: list[str], arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformsiv(arg0: int, arg1: int, arg2: list[int], arg3: int, arg4: int, arg5: list[int], arg6: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformsiv(arg0: int, arg1: int, arg2: IntBuffer, arg3: int, arg4: IntBuffer) -> None: ...
    @staticmethod
    def glGetUniformBlockIndex(arg0: int, arg1: str) -> int: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockiv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockiv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockName(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int, arg5: list[int], arg6: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockName(arg0: int, arg1: int, arg2: Buffer, arg3: Buffer) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockName(arg0: int, arg1: int) -> str: ...
    @staticmethod
    def glUniformBlockBinding(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glDrawArraysInstanced(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @overload
    @staticmethod
    def glDrawElementsInstanced(arg0: int, arg1: int, arg2: int, arg3: Buffer, arg4: int) -> None: ...
    @overload
    @staticmethod
    def glDrawElementsInstanced(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glFenceSync(arg0: int, arg1: int) -> int: ...
    @staticmethod
    def glIsSync(arg0: int) -> bool: ...
    @staticmethod
    def glDeleteSync(arg0: int) -> None: ...
    @staticmethod
    def glClientWaitSync(arg0: int, arg1: int, arg2: int) -> int: ...
    @staticmethod
    def glWaitSync(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGetInteger64v(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGetInteger64v(arg0: int, arg1: LongBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSynciv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int, arg5: list[int], arg6: int) -> None: ...
    @overload
    @staticmethod
    def glGetSynciv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer, arg4: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetInteger64i_v(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetInteger64i_v(arg0: int, arg1: int, arg2: LongBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteri64v(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteri64v(arg0: int, arg1: int, arg2: LongBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenSamplers(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGenSamplers(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteSamplers(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteSamplers(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glIsSampler(arg0: int) -> bool: ...
    @staticmethod
    def glBindSampler(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glSamplerParameteri(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameteriv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameteriv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glSamplerParameterf(arg0: int, arg1: int, arg2: float) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterfv(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterfv(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameteriv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameteriv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterfv(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterfv(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @staticmethod
    def glVertexAttribDivisor(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glBindTransformFeedback(arg0: int, arg1: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteTransformFeedbacks(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteTransformFeedbacks(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenTransformFeedbacks(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGenTransformFeedbacks(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glIsTransformFeedback(arg0: int) -> bool: ...
    @staticmethod
    def glPauseTransformFeedback() -> None: ...
    @staticmethod
    def glResumeTransformFeedback() -> None: ...
    @overload
    @staticmethod
    def glGetProgramBinary(arg0: int, arg1: int, arg2: list[int], arg3: int, arg4: list[int], arg5: int, arg6: Buffer) -> None: ...
    @overload
    @staticmethod
    def glGetProgramBinary(arg0: int, arg1: int, arg2: IntBuffer, arg3: IntBuffer, arg4: Buffer) -> None: ...
    @staticmethod
    def glProgramBinary(arg0: int, arg1: int, arg2: Buffer, arg3: int) -> None: ...
    @staticmethod
    def glProgramParameteri(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glInvalidateFramebuffer(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glInvalidateFramebuffer(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glInvalidateSubFramebuffer(arg0: int, arg1: int, arg2: list[int], arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> None: ...
    @overload
    @staticmethod
    def glInvalidateSubFramebuffer(arg0: int, arg1: int, arg2: IntBuffer, arg3: int, arg4: int, arg5: int, arg6: int) -> None: ...
    @staticmethod
    def glTexStorage2D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glTexStorage3D(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...
    @overload
    @staticmethod
    def glGetInternalformativ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: list[int], arg5: int) -> None: ...
    @overload
    @staticmethod
    def glGetInternalformativ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: IntBuffer) -> None: ...
    @staticmethod
    def glReadPixels(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> None: ...
