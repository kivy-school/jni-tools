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
    def glReadBuffer(p0: int) -> None: ...
    @overload
    @staticmethod
    def glDrawRangeElements(p0: int, p1: int, p2: int, p3: int, p4: int, p5: Buffer) -> None: ...
    @overload
    @staticmethod
    def glDrawRangeElements(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def glTexImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int) -> None: ...
    @overload
    @staticmethod
    def glTexImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: Buffer) -> None: ...
    @overload
    @staticmethod
    def glTexSubImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: int) -> None: ...
    @overload
    @staticmethod
    def glTexSubImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: Buffer) -> None: ...
    @staticmethod
    def glCopyTexSubImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int) -> None: ...
    @overload
    @staticmethod
    def glCompressedTexImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @overload
    @staticmethod
    def glCompressedTexImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int) -> None: ...
    @overload
    @staticmethod
    def glCompressedTexSubImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: int) -> None: ...
    @overload
    @staticmethod
    def glCompressedTexSubImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: Buffer) -> None: ...
    @overload
    @staticmethod
    def glGenQueries(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenQueries(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteQueries(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteQueries(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glIsQuery(p0: int) -> bool: ...
    @staticmethod
    def glBeginQuery(p0: int, p1: int) -> None: ...
    @staticmethod
    def glEndQuery(p0: int) -> None: ...
    @overload
    @staticmethod
    def glGetQueryiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetQueryiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetQueryObjectuiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetQueryObjectuiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glUnmapBuffer(p0: int) -> bool: ...
    @staticmethod
    def glGetBufferPointerv(p0: int, p1: int) -> Buffer: ...
    @overload
    @staticmethod
    def glDrawBuffers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDrawBuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2x3fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2x3fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3x2fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3x2fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2x4fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2x4fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4x2fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4x2fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3x4fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3x4fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4x3fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4x3fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @staticmethod
    def glBlitFramebuffer(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int) -> None: ...
    @staticmethod
    def glRenderbufferStorageMultisample(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glFramebufferTextureLayer(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glMapBufferRange(p0: int, p1: int, p2: int, p3: int) -> Buffer: ...
    @staticmethod
    def glFlushMappedBufferRange(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glBindVertexArray(p0: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteVertexArrays(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteVertexArrays(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenVertexArrays(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGenVertexArrays(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glIsVertexArray(p0: int) -> bool: ...
    @overload
    @staticmethod
    def glGetIntegeri_v(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetIntegeri_v(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glBeginTransformFeedback(p0: int) -> None: ...
    @staticmethod
    def glEndTransformFeedback() -> None: ...
    @staticmethod
    def glBindBufferRange(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glBindBufferBase(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glTransformFeedbackVaryings(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> str: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(p0: int, p1: int, p2: int, p3: IntBuffer, p4: IntBuffer, p5: IntBuffer, p6: int) -> None: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(p0: int, p1: int, p2: IntBuffer, p3: IntBuffer) -> str: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(p0: int, p1: int, p2: int, p3: Any, p4: int, p5: Any, p6: int, p7: Any, p8: int, p9: Any, p10: int) -> None: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(p0: int, p1: int, p2: int, p3: IntBuffer, p4: IntBuffer, p5: IntBuffer, p6: ByteBuffer) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribIPointer(p0: int, p1: int, p2: int, p3: int, p4: Buffer) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribIPointer(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribIiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribIiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribIuiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribIuiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glVertexAttribI4i(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glVertexAttribI4ui(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribI4iv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribI4iv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribI4uiv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribI4uiv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetUniformuiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetUniformuiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glGetFragDataLocation(p0: int, p1: str) -> int: ...
    @staticmethod
    def glUniform1ui(p0: int, p1: int) -> None: ...
    @staticmethod
    def glUniform2ui(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glUniform3ui(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glUniform4ui(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniform1uiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform1uiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform2uiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform2uiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform3uiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform3uiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform4uiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform4uiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glClearBufferiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glClearBufferiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glClearBufferuiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glClearBufferuiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glClearBufferfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glClearBufferfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glClearBufferfi(p0: int, p1: int, p2: float, p3: int) -> None: ...
    @staticmethod
    def glGetStringi(p0: int, p1: int) -> str: ...
    @staticmethod
    def glCopyBufferSubData(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGetUniformIndices(p0: int, p1: Any, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetUniformIndices(p0: int, p1: Any, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformsiv(p0: int, p1: int, p2: Any, p3: int, p4: int, p5: Any, p6: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformsiv(p0: int, p1: int, p2: IntBuffer, p3: int, p4: IntBuffer) -> None: ...
    @staticmethod
    def glGetUniformBlockIndex(p0: int, p1: str) -> int: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockName(p0: int, p1: int, p2: Buffer, p3: Buffer) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockName(p0: int, p1: int, p2: int, p3: Any, p4: int, p5: Any, p6: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockName(p0: int, p1: int) -> str: ...
    @staticmethod
    def glUniformBlockBinding(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glDrawArraysInstanced(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glDrawElementsInstanced(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glDrawElementsInstanced(p0: int, p1: int, p2: int, p3: Buffer, p4: int) -> None: ...
    @staticmethod
    def glFenceSync(p0: int, p1: int) -> int: ...
    @staticmethod
    def glIsSync(p0: int) -> bool: ...
    @staticmethod
    def glDeleteSync(p0: int) -> None: ...
    @staticmethod
    def glClientWaitSync(p0: int, p1: int, p2: int) -> int: ...
    @staticmethod
    def glWaitSync(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetInteger64v(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetInteger64v(p0: int, p1: LongBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSynciv(p0: int, p1: int, p2: int, p3: Any, p4: int, p5: Any, p6: int) -> None: ...
    @overload
    @staticmethod
    def glGetSynciv(p0: int, p1: int, p2: int, p3: IntBuffer, p4: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetInteger64i_v(p0: int, p1: int, p2: LongBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetInteger64i_v(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteri64v(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteri64v(p0: int, p1: int, p2: LongBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenSamplers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenSamplers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteSamplers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteSamplers(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glIsSampler(p0: int) -> bool: ...
    @staticmethod
    def glBindSampler(p0: int, p1: int) -> None: ...
    @staticmethod
    def glSamplerParameteri(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glSamplerParameterf(p0: int, p1: int, p2: float) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glVertexAttribDivisor(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindTransformFeedback(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteTransformFeedbacks(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteTransformFeedbacks(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGenTransformFeedbacks(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenTransformFeedbacks(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glIsTransformFeedback(p0: int) -> bool: ...
    @staticmethod
    def glPauseTransformFeedback() -> None: ...
    @staticmethod
    def glResumeTransformFeedback() -> None: ...
    @overload
    @staticmethod
    def glGetProgramBinary(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int, p6: Buffer) -> None: ...
    @overload
    @staticmethod
    def glGetProgramBinary(p0: int, p1: int, p2: IntBuffer, p3: IntBuffer, p4: Buffer) -> None: ...
    @staticmethod
    def glProgramBinary(p0: int, p1: int, p2: Buffer, p3: int) -> None: ...
    @staticmethod
    def glProgramParameteri(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glInvalidateFramebuffer(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glInvalidateFramebuffer(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glInvalidateSubFramebuffer(p0: int, p1: int, p2: Any, p3: int, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @overload
    @staticmethod
    def glInvalidateSubFramebuffer(p0: int, p1: int, p2: IntBuffer, p3: int, p4: int, p5: int, p6: int) -> None: ...
    @staticmethod
    def glTexStorage2D(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glTexStorage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def glGetInternalformativ(p0: int, p1: int, p2: int, p3: int, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glGetInternalformativ(p0: int, p1: int, p2: int, p3: int, p4: IntBuffer) -> None: ...
    @staticmethod
    def glReadPixels(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int) -> None: ...
